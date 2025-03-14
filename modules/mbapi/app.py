from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import json
import threading
import os
from kafka.errors import TopicAlreadyExistsError


app = Flask(__name__)

# Get Kafka server from environment (set by Docker Compose)
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'localhost:9092')
TOPIC_NAME = 'test-topic'



# Function to create Kafka topic if it doesn't exist
def create_topic_if_not_exists():
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)
    try:
        # Check if the topic exists; create if it doesn't
        topics = admin_client.list_topics()
        if TOPIC_NAME not in topics:
            topic = NewTopic(name=TOPIC_NAME, num_partitions=1, replication_factor=1)
            admin_client.create_topics([topic])
            print(f"✅ Topic '{TOPIC_NAME}' created!")
        else:
            print(f"✅ Topic '{TOPIC_NAME}' already exists!")
    except Exception as e:
        print(f"❌ Error while checking/creating topic: {str(e)}")
    finally:
        admin_client.close()

# Create the topic when the app starts
create_topic_if_not_exists()


# Setup Kafka producer with kafka-python
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)




# Cache messages temporarily
messages_cache = []

# Background Kafka consumer to fetch messages continuously
def consume_messages():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER,
        group_id='flask-consumer',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("✅ Consumer started, listening for messages...")
    for message in consumer:
        messages_cache.append(message.value)
        print(f"📩 Received: {message.value}")

# Start the Kafka consumer in a background thread
threading.Thread(target=consume_messages, daemon=True).start()


# POST endpoint to send messages
@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        message = data.get('message')

        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Send message to Kafka topic
        producer.send(TOPIC_NAME, {'message': message})
        producer.flush()

        return jsonify({"status": "Message sent", "message": message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET endpoint to retrieve messages
@app.route('/get-messages', methods=['GET'])
def get_messages():
    try:
        if not messages_cache:
            return jsonify({"status": "No messages found"}), 200

        return jsonify({"messages": messages_cache}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
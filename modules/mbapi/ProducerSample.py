from kafka import KafkaProducer

TOPIC_NAME = 'test-topic'
KAFKA_SERVER = 'localhost:9092'

# Ensure value_serializer to handle string messages properly
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: v.encode('utf-8')
)

# Send the message
print(f"Sending message to '{TOPIC_NAME}'...")
future = producer.send(TOPIC_NAME, value="Test Message!!!")

# Block until a response comes back (handles errors)
try:
    record_metadata = future.get(timeout=10)
    print(f"Message sent to {record_metadata.topic} partition {record_metadata.partition}")
except Exception as e:
    print(f"Failed to send message: {e}")

# Clean up
producer.flush()
producer.close()
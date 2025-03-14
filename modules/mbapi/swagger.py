from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version="1.0", title="Item API", description="A simple Item API")

item_model = api.model("Item", {
    "id": fields.String(description="Unique Item ID"),
    "name": fields.String(description="Item Name")
})

@api.route("/items/<item_id>")
@api.param("item_id", "Unique Item ID", _in="query")
class ItemResource(Resource):
    @api.marshal_with(item_model)
    def get(self, item_id):
        """Get an item by ID"""
        return {"id": item_id, "name": "Sample Item"}

if __name__ == "__main__":
    app.run(debug=True)
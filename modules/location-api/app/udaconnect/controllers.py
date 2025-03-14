from datetime import datetime

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import ConnectionService, LocationService, PersonService
from flask import request,jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import grpc
from concurrent import futures
import location_pb2
import location_pb2_grpc

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnectLocations", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<int:location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    
    # Get all locations or one by ID
    @responds(schema=LocationSchema, many=True)
    def get(self, location_id=None) -> List[Location]:
        if location_id:
            location = LocationService.retrieve(location_id)
            return [location] if location else []
        else:
            locations = LocationService.retrieve_all()
            return locations

    # Create a new location
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        location_data = request.get_json()
        #print(f"Received data: {location_data}")
        location: Location = LocationService.create(location_data)
        return location
        #return jsonify(location_data)










import grpc
from concurrent import futures
import location_pb2
import location_pb2_grpc
from datetime import datetime
from app.udaconnect.services import LocationService

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def CreateLocation(self, request, context):
        location_data = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": datetime.strptime(request.creation_time, "%Y-%m-%dT%H:%M:%S")
        }
        location = LocationService.create(location_data)
        return location_pb2.Location(
            id=location.id,
            person_id=location.person_id,
            longitude=location.longitude,
            latitude=location.latitude,
            creation_time=location.creation_time.isoformat()
        )
    
    def GetLocation(self, request, context):
        location = LocationService.retrieve(request.id)
        if location:
            return location_pb2.Location(
                id=location.id,
                person_id=location.person_id,
                longitude=location.longitude,
                latitude=location.latitude,
                creation_time=location.creation_time.isoformat()
            )
        return location_pb2.Location()  # Return empty if not found
    
    def GetAllLocations(self, request, context):
        locations = LocationService.retrieve_all()
        location_list = [location_pb2.Location(
            id=loc.id,
            person_id=loc.person_id,
            longitude=loc.longitude,
            latitude=loc.latitude,
            creation_time=loc.creation_time.isoformat()) for loc in locations]
        return location_pb2.LocationList(locations=location_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
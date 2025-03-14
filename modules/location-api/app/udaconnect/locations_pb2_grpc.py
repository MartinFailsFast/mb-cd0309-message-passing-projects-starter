# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import locations_pb2 as locations__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in locations_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LocationServiceStub(object):
    """The service that handles location operations
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateLocation = channel.unary_unary(
                '/location.LocationService/CreateLocation',
                request_serializer=locations__pb2.Location.SerializeToString,
                response_deserializer=locations__pb2.Location.FromString,
                _registered_method=True)
        self.GetLocation = channel.unary_unary(
                '/location.LocationService/GetLocation',
                request_serializer=locations__pb2.Location.SerializeToString,
                response_deserializer=locations__pb2.Location.FromString,
                _registered_method=True)


class LocationServiceServicer(object):
    """The service that handles location operations
    """

    def CreateLocation(self, request, context):
        """RPC to create a location
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocation(self, request, context):
        """RPC to get a location by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLocation,
                    request_deserializer=locations__pb2.Location.FromString,
                    response_serializer=locations__pb2.Location.SerializeToString,
            ),
            'GetLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocation,
                    request_deserializer=locations__pb2.Location.FromString,
                    response_serializer=locations__pb2.Location.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'location.LocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('location.LocationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LocationService(object):
    """The service that handles location operations
    """

    @staticmethod
    def CreateLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/location.LocationService/CreateLocation',
            locations__pb2.Location.SerializeToString,
            locations__pb2.Location.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/location.LocationService/GetLocation',
            locations__pb2.Location.SerializeToString,
            locations__pb2.Location.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

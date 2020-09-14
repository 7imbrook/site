# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import send_message_service_pb2 as protos_dot_send__message__service__pb2


class SendMessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendTextSMS = channel.unary_unary(
                '/send_message_service.SendMessage/sendTextSMS',
                request_serializer=protos_dot_send__message__service__pb2.SMSRequest.SerializeToString,
                response_deserializer=protos_dot_send__message__service__pb2.SMSResponse.FromString,
                )


class SendMessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendTextSMS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SendMessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendTextSMS': grpc.unary_unary_rpc_method_handler(
                    servicer.sendTextSMS,
                    request_deserializer=protos_dot_send__message__service__pb2.SMSRequest.FromString,
                    response_serializer=protos_dot_send__message__service__pb2.SMSResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'send_message_service.SendMessage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SendMessage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendTextSMS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/send_message_service.SendMessage/sendTextSMS',
            protos_dot_send__message__service__pb2.SMSRequest.SerializeToString,
            protos_dot_send__message__service__pb2.SMSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
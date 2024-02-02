# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import src.apps.ecommerce.grpc.protobuf.ecommerce__product_pb2 as ecommerce____product__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ProductControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/ecommerce__product.ProductController/List',
                request_serializer=ecommerce____product__pb2.ProductListRequest.SerializeToString,
                response_deserializer=ecommerce____product__pb2.Product.FromString,
                )
        self.Create = channel.unary_unary(
                '/ecommerce__product.ProductController/Create',
                request_serializer=ecommerce____product__pb2.Product.SerializeToString,
                response_deserializer=ecommerce____product__pb2.Product.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/ecommerce__product.ProductController/Retrieve',
                request_serializer=ecommerce____product__pb2.ProductRetrieveRequest.SerializeToString,
                response_deserializer=ecommerce____product__pb2.Product.FromString,
                )
        self.Update = channel.unary_unary(
                '/ecommerce__product.ProductController/Update',
                request_serializer=ecommerce____product__pb2.Product.SerializeToString,
                response_deserializer=ecommerce____product__pb2.Product.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/ecommerce__product.ProductController/Destroy',
                request_serializer=ecommerce____product__pb2.Product.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ProductControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=ecommerce____product__pb2.ProductListRequest.FromString,
                    response_serializer=ecommerce____product__pb2.Product.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=ecommerce____product__pb2.Product.FromString,
                    response_serializer=ecommerce____product__pb2.Product.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=ecommerce____product__pb2.ProductRetrieveRequest.FromString,
                    response_serializer=ecommerce____product__pb2.Product.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=ecommerce____product__pb2.Product.FromString,
                    response_serializer=ecommerce____product__pb2.Product.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=ecommerce____product__pb2.Product.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce__product.ProductController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ecommerce__product.ProductController/List',
            ecommerce____product__pb2.ProductListRequest.SerializeToString,
            ecommerce____product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce__product.ProductController/Create',
            ecommerce____product__pb2.Product.SerializeToString,
            ecommerce____product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce__product.ProductController/Retrieve',
            ecommerce____product__pb2.ProductRetrieveRequest.SerializeToString,
            ecommerce____product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce__product.ProductController/Update',
            ecommerce____product__pb2.Product.SerializeToString,
            ecommerce____product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce__product.ProductController/Destroy',
            ecommerce____product__pb2.Product.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
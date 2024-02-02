# gRPC Controllers
from src.apps.account.grpc.protobuf import user_pb2_grpc
from src.apps.ecommerce.grpc.protobuf import ecommerce__product_pb2_grpc
# gRPC Services
from src.apps.account.grpc.services import UserService 
from src.apps.ecommerce.grpc.services import ProductService 


def grpc_handlers(server):
    user_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    ecommerce__product_pb2_grpc.add_ProductControllerServicer_to_server(ProductService.as_servicer(), server)

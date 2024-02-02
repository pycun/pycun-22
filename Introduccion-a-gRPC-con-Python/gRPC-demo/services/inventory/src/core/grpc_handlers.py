# gRPC Controllers
from src.apps.account.grpc.protobuf import user_pb2_grpc
from src.apps.inventory.grpc.protobuf import product_pb2_grpc, inventory_pb2_grpc
# gRPC Services
from src.apps.account.grpc.services import UserService
from src.apps.inventory.grpc.services import ProductService, InventoryService

def grpc_handlers(server):
    user_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    product_pb2_grpc.add_ProductControllerServicer_to_server(ProductService.as_servicer(), server)
    inventory_pb2_grpc.add_InventoryControllerServicer_to_server(InventoryService.as_servicer(), server)

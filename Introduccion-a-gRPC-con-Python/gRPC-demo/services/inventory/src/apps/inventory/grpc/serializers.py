from django_grpc_framework import proto_serializers

from src.apps.inventory.models import Product, Inventory
from src.apps.inventory.grpc.protobuf import product_pb2, inventory_pb2



class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = product_pb2.Product
        fields = ['id', 'name', 'price', 'description']


class InventoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Inventory
        proto_class = inventory_pb2.Inventory
        fields = ['id', 'quantity', 'product']

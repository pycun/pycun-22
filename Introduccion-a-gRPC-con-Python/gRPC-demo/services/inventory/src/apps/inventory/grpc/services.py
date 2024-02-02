from django_grpc_framework import generics

from src.apps.inventory.models import Product, Inventory
from src.apps.inventory.grpc.serializers import ProductProtoSerializer, InventoryProtoSerializer



class ProductService(generics.ModelService):
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer



class InventoryService(generics.ModelService):
    queryset = Inventory.objects.all()
    serializer_class = InventoryProtoSerializer

from django_grpc_framework import generics

from src.apps.ecommerce.models import Product
from src.apps.ecommerce.grpc.serializers import ProductProtoSerializer


class ProductService(generics.ModelService):
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer

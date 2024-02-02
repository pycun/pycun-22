from django_grpc_framework import proto_serializers

from src.apps.ecommerce.models import Product
from src.apps.ecommerce.grpc.protobuf import ecommerce__product_pb2


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = ecommerce__product_pb2.Product
        fields = ['folio', 'name', 'price']
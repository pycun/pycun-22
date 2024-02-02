from rest_framework import viewsets
from src.apps.inventory.models import Product
from src.apps.inventory.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

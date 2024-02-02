import uuid
import grpc
from django.conf import settings
from django.db import models

from src.apps.ds_ecommerce.grpc.protobuf import ecommerce__product_pb2_grpc, ecommerce__product_pb2


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    product = models.OneToOneField('inventory.Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.product.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        with grpc.insecure_channel(settings.ECOMMERCE_GRPC_SERVER_ADDRESS) as channel:
            stub = ecommerce__product_pb2_grpc.ProductControllerStub(channel)
    
            # Si es un nuevo producto, debemos crearlo en el servicio de ecommerce
            grps_message = ecommerce__product_pb2.Product(
                folio=str(self.pk),
                name=self.name,
                price=str(self.price),
            )
            response = stub.Create(grps_message)


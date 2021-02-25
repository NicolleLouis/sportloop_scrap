from django.db import models
from django.contrib import admin

from campsider.models.seller import Seller


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.TextField()
    seller = models.ForeignKey(
        Seller,
        null=True,
        default=None,
        verbose_name="seller",
        on_delete=models.SET_NULL
    )
    price = models.FloatField()
    postal_code = models.IntegerField()

    def __str__(self):
        return "{} from {}".format(self.name, self.seller.name)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "postal_code"
    )

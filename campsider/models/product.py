from django.db import models
from django.contrib import admin

from campsider.models.seller import Seller


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    url = models.TextField()
    seller = models.ForeignKey(
        Seller,
        null=True,
        blank=True,
        default=None,
        verbose_name="seller",
        on_delete=models.SET_NULL
    )
    price = models.FloatField(
        null=True,
        blank=True,
    )
    postal_code = models.IntegerField(
        null=True,
        blank=True,
    )
    is_scrapped = models.BooleanField(
        default=False
    )
    date_scrap = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        seller_name = self.seller.name if self.seller else 'Unknown'
        return "{} from {}".format(str(self.name), str(seller_name))


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'is_scrapped',
        "name",
        "price",
        "postal_code"
    )

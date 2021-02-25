from django.db import models
from django.contrib import admin


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class SellerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

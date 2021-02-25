from django.contrib import admin

from django.contrib.auth.models import User, Group
from .models.seller import Seller, SellerAdmin
from .models.product import ProductAdmin, Product

# Register your models here.
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)

# Clean useless model
admin.site.unregister(User)
admin.site.unregister(Group)

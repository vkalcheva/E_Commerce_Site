from django.contrib import admin

# Register your models here.
from e_commerce_site.shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


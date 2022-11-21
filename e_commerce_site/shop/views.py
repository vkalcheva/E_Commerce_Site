from django.shortcuts import render

from e_commerce_site.shop.models import Product


def index(request):
    product_objects = Product.objects.all()
    context = {
        'product_objects': product_objects,
    }
    return render(request, 'shop/index.html', context)

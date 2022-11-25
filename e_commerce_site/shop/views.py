from django.core.paginator import Paginator
from django.shortcuts import render

from e_commerce_site.shop.models import Product


def index(request):
    product_objects = Product.objects.all()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    #paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    context = {
        'product_objects': product_objects,
    }
    return render(request, 'shop/index.html', context)

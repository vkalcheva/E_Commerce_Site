from django.urls import path

from e_commerce_site.shop.views import index

urlpatterns = (
    path('', index, name='index'),
)
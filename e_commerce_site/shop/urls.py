from django.urls import path

from e_commerce_site.shop.views import index, detail

urlpatterns = (
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
)
from django.urls import path

from e_commerce_site.shop import views


urlpatterns = (
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
)
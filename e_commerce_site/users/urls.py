from django.urls import path

from e_commerce_site.users import views

urlpatterns = (
    path('', views.profiles, name='profiles'),

)
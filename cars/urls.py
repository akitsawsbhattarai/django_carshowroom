
from django.urls import path
from .views import *

app_name = "cars"

urlpatterns = [
    path('', Home.as_view(), name='home' ),
    path('create_brand/', Create_brands.as_view() , name='brand_create'),
    path('create_car/', Create_cars.as_view() , name='car_create'),
    path('update_car/<int:pk>',Update_car.as_view(),name='update_car'),
    path('delete_car/<int:pk>',Delete_car.as_view(),name='car_delete'),
  
]



from django.urls import path

from .views import *


app_name = "cars"

urlpatterns = [
    path('', Home.as_view(), name='home' ),
    path('brand/', Brandlist.as_view() , name='brand'),
    path('car/', Car.as_view() , name='car'),

    path('create-brand/', create_brands , name='brand_create'),
    path('car/add/', Create_cars.as_view() , name='car_create'),
    path('update-car/<int:pk>',Update_car.as_view(),name='update_car'),
    path('update-brand/<int:pk>',Update_brand.as_view(),name='update_brand'),
    path('delete-car/<int:pk>',Delete_car.as_view(),name='car_delete'),
    path('delete-brand/<int:pk>',Delete_brand.as_view(),name='brand_delete'),
    path('dashboard/', Dashboard.as_view(), name='dashboard' ),

]


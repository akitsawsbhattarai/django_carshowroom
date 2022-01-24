from asyncio.windows_events import NULL
from contextlib import nullcontext
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Brand(models.Model):
    class Meta():
        db_table='brand_tbl'
        
    name=models.CharField(max_length=50, unique=True)
    # logo=models.ImageField(upload_to='logo/',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        name=f'--{self.name}--'
        return name


class Cars(models.Model):
    class Meta():
        db_table='cars_tbl'
        verbose_name="car"
        verbose_name_plural="cars"
        
    name=models.CharField(max_length=50, unique=True)
    image=models.ImageField(upload_to='carimages/',blank=True, null=True)
    price=models.CharField(max_length=50)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    brand=models.ForeignKey(Brand,related_name='brand_car', on_delete=models.CASCADE)

    def __str__(self):
        name=self.name
        return name
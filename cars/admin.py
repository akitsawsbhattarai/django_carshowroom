from django.contrib import admin

from .models.models import Brand, Cars

# Register your models here.

@admin.register(Brand)
class Brand(admin.ModelAdmin):
    pass

@admin.register(Cars)
class Cars(admin.ModelAdmin):
    pass

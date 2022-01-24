from django.forms import ModelForm, fields
from .models.models import Brand, Cars

class Brandform(ModelForm):
    class Meta():
        model=Brand
        fields='__all__'

class Carform(ModelForm):
    class Meta():
        model=Cars
        fields='__all__'
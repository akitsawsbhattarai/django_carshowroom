from django.forms import ModelForm, fields, Form
from .models.models import Brand, Cars, UserRegister

class Brandform(ModelForm):
    class Meta():
        model=Brand
        fields='__all__'

class Carform(ModelForm):
    class Meta():
        model=Cars
        fields='__all__'

class UserRegisterform(ModelForm):
    class Meta():
        model=UserRegister
        fields='__all__'
        
class LoginForm(Form):
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)
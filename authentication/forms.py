from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
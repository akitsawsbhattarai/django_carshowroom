from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)    
            return redirect(reverse('cars:home'))
            messages.success(request, 'Account created successfully!')
        else:
            messages.error(request, 'Error creating account')
    return render(request, 'login.html')
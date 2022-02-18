
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import  messages

from cars.form import UserRegisterform

    
def userlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('cars:home')
        else:
            messages.error(request,'invalid input')
    context={
        'href':'signup/',
        'msg1':'Register a new membership',
        'msg2':'I forgot my password',
        'button':'Sign In'

    }

    return render(request,'login.html',context)


def userlogout(request):
    logout(request)
    return redirect('loginuser')
    

def usersignup(request):
    if request.method=='POST':
        form=UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You may now login.')
            login(request,user)
            return redirect('cars:home') 
        messages.error(request,'invalid username or password')

    context={
        'href':'login/',
        'msg1':'Already have account?',
        'button':'Sign Up'
    }
    return render(request,'login.html',context)

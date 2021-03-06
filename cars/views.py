from audioop import reverse
from django.urls import reverse_lazy
from dataclasses import field
from re import template
from django.shortcuts import redirect, render
from .models.models import Brand,Cars
from .form  import Brandform, Carform
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.

# CREATE

def create_brands(request):
    form=Brandform()
    if request.method=="POST":
        form=Brandform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:home')
    context = {
        "title": "Create Form",
        "form": form,
        'titlebrand':'Brands',
        'brands': Brand.objects.all(),
    }
    return render(request, 'create_brand.html', context)

# def create_cars(request):
#     form=Carform()
#     if request.method=="POST":
#         form=Carform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cars:home')
#     context = {
#         "title": "Create Form",
#         "form": form
#     }
#     return render(request, 'create_car.html', context)

# # class based view

class Create_cars(CreateView):
    login_url = '/login/'
    model=Cars
    template_name='create_car.html'
    form=Carform
    fields='__all__'
    context_object_name='form'
    success_url = reverse_lazy('cars:home')

    def get_success_url(self):
        return super().get_success_url()

# class Create_brands(CreateView):
#     model=Brand
#     template_name='create_brand.html'
#     form=Brandform
#     fields='__all__'
#     context_object_name='form'
#     success_url = reverse_lazy('cars:home')

#     def get_context_data(self,form):
#         context= super().get_context_data(form)
#         context['form']=Brandform
#         context['brands']= Brand.objects.all()
#         context['titlebrand']= 'Brands'
#         context['titlecar']= 'Cars'
#         context['cars']= Cars.objects.all()

#         return context
    




# READ
# def home(request):
#     brands=Brand.objects.all()
#     cars=Cars.objects.all()
#     context={
#         'titlebrand':'Brands',
#         'brands': brands,
#         'titlecar':'Cars',
#         'cars':cars
#     }
#     return render(request,'home.html',context=context)

class Brandlist(ListView):
    model=Brand
    login_url = '/login/'
    template_name='brand.html'
    context_object_name='brands'

class Car(ListView):
    login_url = '/login/'
    model=Cars
    template_name='car.html'
    context_object_name='cars'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']= 'Car'
        return context

class Home(ListView):
    login_url = '/login/'
    model=Cars
    template_name='home.html'
    # context_object_name='cars'

    def get_context_data(self):
        context= super().get_context_data()
        
        context={
            'title': 'Dashboard',
            'brands': Brand.objects.all,
            'cars':Cars.objects.all()
        }
        return context



# UPDATE

# def update_car(request, id):
#     car=Cars.objects.get(id=id)
#     form=Carform(instance=car)
#     if request.method=='POST':
#         form=Carform(request.POST,request.FILES,instance=car)
#         if form.is_valid():
#             form.save()
#             return redirect('cars:home')
#     context={
#         'title':'Update Form',
#         'form':form
#     }
#     return render(request, 'create_car.html', context)
    
class Update_car(UpdateView):
    model=Cars
    form=Carform
    fields='__all__'
    template_name='create_car.html'
    context_object_name='form'
    success_url = reverse_lazy('cars:home')

class Update_brand(UpdateView):
    model=Brand
    form=Brandform
    fields='__all__'
    template_name='create_brand.html'
    context_object_name='form'
    success_url = reverse_lazy('cars:home')


# DELETE
        
# def delete_car(request, id):
#     if request.method=='POST':
#         car=Cars.objects.get(id=id)
#         car.delete()
#     return redirect('cars:home')

class Delete_car(DeleteView):
    model=Cars
    success_url = reverse_lazy('cars:home')

class Delete_brand(DeleteView):
    model=Brand
    success_url = reverse_lazy('cars:home')


class Dashboard(ListView):
    model=Cars
    template_name ="dashboard.html"

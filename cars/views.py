from re import template
from django.shortcuts import redirect, render
from .models.models import Brand,Cars
from .form  import Brandform, Carform
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.

# CREATE
# def create_brands(request):
#     form=Brandform()
#     if request.method=="POST":
#         form=Brandform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cars:home')
#     context = {
#         "title": "Create Form",
#         "form": form
#     }
#     return render(request, 'create_brand.html', context)

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
    model=Cars
    template_name='create_car.html'
    form=Carform
    context_object_name='form'

class Create_brands(CreateView):
    model=Brand
    template_name='create_brand.html'
    form=Brandform
    context_object_name='form'
    




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

class Home(ListView):
    model=Cars
    template_name='home.html'
    context_object_name='cars'

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
    template_name='create_car.html'
    context_object_name='form'



# DELETE
        
# def delete_car(request, id):
#     if request.method=='POST':
#         car=Cars.objects.get(id=id)
#         car.delete()
#     return redirect('cars:home')

class Delete_car(DeleteView):
    model=Cars
    

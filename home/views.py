from django.shortcuts import render
from category.models import Category
from flat_creation.models import Flat_create
from itertools import zip_longest

def index(request):
    data = Category.objects.all()
    cat = {'all_cat':data}
    return render (request , 'user/home.html', cat)

def product_list(request,id):
    flat_obj = Flat_create.objects.filter(rent_id_id=id)
    flat_obj = {'all_flat':flat_obj}
    return render (request , 'user/product_list.html', flat_obj)

def details(request,id):
    flat_obj = Flat_create.objects.get(id=id)
    flat_obj = {'all_flat1':flat_obj}
    return render(request, 'user/detail.html', flat_obj)

# Create your views here.

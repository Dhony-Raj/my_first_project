from django.shortcuts import render
from category.models import Category
from flat_creation.models import Flat_create
from itertools import zip_longest

def index(request):
    data = Category.objects.all()
    data2 = Flat_create.objects.order_by('-pk')[:5]
    data3 = Flat_create.objects.filter(rent_id_id=1).order_by('-pk')[:4]
    data4 = Flat_create.objects.order_by('-dis_flat')[:4]
    length = len(data3)
    length = length !=0
    print("asdasdasdasdasdasdasdasdasdasdadasdasdadasdasdasdd",length)
    cat = {'all_cat':data, 'data2':data2, 'data3':data3, 'data4':data4, 'size1':length}
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

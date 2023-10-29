from django.shortcuts import render,redirect,HttpResponse
from .models import Category

def category(request):
    return render(request, 'admin/category.html')

def cat_input(request):
    cat_num = request.POST.get('cat_num')

    cat_obj = Category()
    cat_obj.cat_num = cat_num

    cat_obj.save()

    return redirect('home1')

# Create your views here.

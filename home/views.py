from django.shortcuts import render
from category.models import Category

def index(request):
    data = Category.objects.all()
    cat = {'all_cat':data}
    return render (request , 'user/home.html', cat)

# Create your views here.

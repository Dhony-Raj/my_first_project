from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from category.models import Category
from .models import Flat_create


def flat(request):
            all_cat = Category.objects.all().order_by('-id')
            flat = Flat_create.objects.all().order_by('-id')
            data = {'cat_data':all_cat, 'flat': flat}
            return render(request, 'admin/flat.html', data)
def input(request):
    rent_id  = request.POST.get('rent_id')
    flat_num = request.POST.get('flat_num')
    floor_num = request.POST.get('floor_num')
    nor_name = request.POST.get('nor_name')
    room_size = request.POST.get('room_size')
    flat_price = request.POST.get('flat_price')
    flat_discount = request.POST.get('flat_dis')
    module = request.POST.get('module')
    room_pic = request.FILES.get('room_pic')
    discount_price = request.FILES.get('discount_price')



    category = get_object_or_404(Category, pk=rent_id)
    flat_obj = Flat_create()
    flat_obj.rent_id = category
    flat_obj.flat_num = flat_num
    flat_obj.floor_num = floor_num
    flat_obj.nor_name = nor_name
    flat_obj.room_size = room_size
    flat_obj.flat_price = flat_price
    flat_obj.flat_discount = flat_discount
    flat_obj.module = module
    flat_obj.room_pic = room_pic
    flat_obj.discount_price = discount_price

    flat_obj.save()

    return redirect('home')
                
            
# Create your views here.

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
    flat_name = request.POST.get('flat_name')
    flat_num = request.POST.get('flat_num')
    floor_num = request.POST.get('floor_num')
    nor_name = request.POST.get('nor_name')
    room_size = request.POST.get('room_size')
    flat_price = request.POST.get('flat_price')
    flat_discount = request.POST.get('flat_dis')
    flat_details = request.POST.get('flat_details')
    room_pic = request.FILES.get('room_pic')
    flat_dis = request.FILES.get('flat_dis')



    # category = get_object_or_404(Category, pk=rent_id)
    flat_obj = Flat_create()
    flat_obj.rent_id_id = rent_id
    flat_obj.flat_name = flat_name
    flat_obj.flat_num = flat_num
    flat_obj.floor_num = floor_num
    flat_obj.nor_name = nor_name
    flat_obj.room_size = room_size
    flat_obj.flat_price = flat_price
    flat_obj.flat_discount = flat_discount
    flat_obj.flat_details = flat_details
    flat_obj.room_pic = room_pic
    flat_obj.flat_dis = flat_dis

    flat_obj.save()

    return redirect('home')


def update(request,id):
    all_cat = Category.objects.all().order_by('-id')
    flat_obj = Flat_create.objects.get(id=id)
    single_flat = {'flat_data':flat_obj,'cat_data':all_cat, 'id':id}
    return render(request, 'admin/edit_flat.html',single_flat)

def update1(request):
    rent_id  = request.POST.get('rent_id')
    flat_name = request.POST.get('flat_name')
    flat_num = request.POST.get('flat_num')
    floor_num = request.POST.get('floor_num')
    nor_name = request.POST.get('nor_name')
    room_size = request.POST.get('room_size')
    flat_price = request.POST.get('flat_price')
    flat_discount = request.POST.get('flat_dis')
    flat_details = request.POST.get('flat_details')
    room_pic = request.FILES.get('room_pic')
    flat_dis = request.FILES.get('flat_dis')

    flat_obj = Flat_create.objects.get(id=rent_id)
    flat_obj.flat_name = flat_name
    flat_obj.flat_num = flat_num
    flat_obj.floor_num = floor_num
    flat_obj.nor_name = nor_name
    flat_obj.room_size = room_size
    flat_obj.flat_price = flat_price
    flat_obj.flat_discount = flat_discount
    flat_obj.flat_details = flat_details
    flat_obj.room_pic = room_pic
    flat_obj.flat_dis = flat_dis

    flat_obj.save()
    return redirect('home')


def delete_flat(request,id):
    flat_obj = Flat_create.objects.get(id=id)
    flat_obj.delete() #delete from table where id=id
    return redirect('home')
                
            
# Create your views here.

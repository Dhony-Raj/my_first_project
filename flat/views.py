from django.shortcuts import render,HttpResponse,redirect
from .models import Flat

def flat(request):
    flat = Flat.objects.all().order_by('-id')
    data = {'flat_data':flat}
    return render(request, './flat.html', data)

def input(request):
    flat_num = request.POST.get('flat_num')
    floor_num = request.POST.get('floor_num')
    nor_name = request.POST.get('nor_name')
    room_size = request.POST.get('room_size')
    flat_price = request.POST.get('flat_price')
    flat_discount = request.POST.get('flat_dis')
    module = request.POST.get('module')
    room_pic = request.FILES.get('room_pic')

    flat_obj = Flat()
    flat_obj.flat_num = flat_num
    flat_obj.floor_num = floor_num
    flat_obj.nor_name = nor_name
    flat_obj.room_size = room_size
    flat_obj.flat_price = flat_price
    flat_obj.flat_discount = flat_discount
    flat_obj.module = module
    flat_obj.room_pic = room_pic

    flat_obj.save()

    return redirect('home')

# Create your views here.

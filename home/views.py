from django.shortcuts import render
from category.models import Category
from flat_creation.models import Flat_create

def index(request):
    data = Category.objects.all()
    cat = {'all_cat':data}
    return render (request , 'user/home.html', cat)

def product_list(request,id):
    flat_obj = Flat_create.objects.filter(rent_id_id=id)
    discount_price_list =[]
    for i in flat_obj:
        print(i)
        print("duf",i.flat_price)
        print("uwfenu",i.flat_discount)
        discount_fee = flat_price - ((flat_price * flat_discount)/100)
        discount_price_list.append(discount_fee)

        flat_obj1 = {'all_flat':flat_obj , 'discount':discount_price_list}


    # flat_obj = {'all_flat':flat_obj}
    return render (request , 'user/product_list.html', flat_obj1)

# Create your views here.

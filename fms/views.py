from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Renter


def index(request):
    return render(request, 'admin/index.html')

def details(request):
        rent_obj = Renter()
        rent_obj.name = request.POST.get('rent_name')
        rent_obj.phone_number1 = request.POST.get('phone1_name')
        rent_obj.phone_number2 = request.POST.get('phone2_name')
        rent_obj.email = request.POST.get('email_name')
        rent_obj.number_of_members = request.POST.get('nfm_name')
        rent_obj.nid_number = request.POST.get('nid_name')
        rent_obj.user_name = request.POST.get('user_name')
        
        rent_obj.save()

        return redirect('home')

    




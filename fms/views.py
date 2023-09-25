from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Renter
from django.contrib import messages


def index(request):
    renter = Renter.objects.all().order_by('-id')
    rent_data = {'data':renter}
    return render(request, 'admin/index.html',rent_data)

def details(request):
      rent_name = request.POST.get('rent_name')
      phone1_name = request.POST.get('phone1_name')
      phone2_name = request.POST.get('phone2_name')
      email_name = request.POST.get('email_name')
      nfm_name = request.POST.get('nfm_name')
      nid_name = request.POST.get('nid_name')
      user_name = request.POST.get('user_name')
      data = (rent_name,phone1_name,phone2_name,email_name,nfm_name,nid_name,user_name)
      renter_data = {'data': data}
      if renter_data:
            if len(rent_name)==0:
                  messages.success(request, 'Name can not be empty')
            elif len(phone1_name)!=11:
                  messages.success(request, 'The phone number 1 must be 11')
            elif len(phone2_name)!=11:
                  messages.success(request, 'The phone number 2 must be 11')
            elif len(email_name)==0:
                  messages.success(request, 'Email can not be empty')
            elif len(nfm_name)==0:
                  messages.success(request, 'Number of members can not be empty')
            elif len(nid_name)==0:
                  messages.success(request, 'NID number can not be empty')
            elif len(user_name)==0:
                  messages.success(request, 'User Name can not be empty')
            elif Renter.objects.filter(name=user_name).exists():
                  messages.success(request, 'This value already exists.')
            else:
                  rent_obj = Renter()
                  rent_obj.name = rent_name
                  rent_obj.phone_number1 = phone1_name
                  rent_obj.phone_number2 = phone2_name
                  rent_obj.email = email_name
                  rent_obj.number_of_members = nfm_name
                  rent_obj.nid_number = nid_name
                  rent_obj.user_name = user_name

                  rent_obj.save()
                  messages.success(request, 'Data Inserted successfully') 

      else:
          messages.success(request, 'Those fields can not be empty')

      return redirect('home')




def edit(request,id):
      rent_obj = Renter.objects.get(id=id)
      single_rent = {'rent_data':rent_obj,'id':id}
      return render(request, 'admin/edit.html',single_rent)

def update(request):
      rent_name = request.POST.get('rent_name')
      phone1_name = request.POST.get('phone1_name')
      phone2_name = request.POST.get('phone2_name')
      email_name = request.POST.get('email_name')
      nfm_name = request.POST.get('nfm_name')
      nid_name = request.POST.get('nid_name')
      user_name = request.POST.get('user_name')
      rent_id = request.POST.get('rent_id')
      data = (rent_name,phone1_name,phone2_name,email_name,nfm_name,nid_name,user_name)
      if data:
            if len(rent_name)==0:
                  messages.success(request, 'Name can not be empty')
            elif len(phone1_name)!=0:
                  messages.success(request, 'The phone number 1 can not be empty')
            elif len(phone1_name)!=11:
                  messages.success(request, 'The phone number 1 must be 11')
            elif len(phone2_name)!=0:
                  messages.success(request, 'The phone number 2 can not be empty')
            elif len(phone2_name)!=11:
                  messages.success(request, 'The phone number 2 must be 11')
            elif len(email_name)==0:
                  messages.success(request, 'Email can not be empty')
            elif len(nfm_name)==0:
                  messages.success(request, 'Number of members can not be empty')
            elif len(nid_name)==0:
                  messages.success(request, 'NID number can not be empty')
            elif len(user_name)==0:
                  messages.success(request, 'User Name can not be empty')
            elif Renter.objects.filter(name=user_name).exists():
                  messages.success(request, 'This value already exists.')
            else:
                  rent_obj = Renter.objects.get(id=rent_id)
                  rent_obj.name = rent_name
                  rent_obj.phone_number1 = phone1_name
                  rent_obj.phone_number2 = phone2_name
                  rent_obj.email = email_name
                  rent_obj.number_of_members = nfm_name
                  rent_obj.nid_number = nid_name
                  rent_obj.user_name = user_name

                  rent_obj.save()
                  messages.success(request, 'Data updated successfully') 

      else:
          messages.success(request, 'Those fields can not be empty')

      return redirect('home')



def delete(request,id):
      rent_obj = Renter.objects.get(id=id)
      rent_obj.delete() #delete from table where id=id
      return redirect('home')
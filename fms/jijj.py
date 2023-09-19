# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import Renter
# from django.contrib import messages


# def index(request):
#     renter = Renter.objects.all().order_by('-id')
#     rent_data = {'data':renter}
#     return render(request, 'admin/index.html',rent_data)

# def details(request):
#         rent_obj = Renter()
#         rent_obj.name = request.POST.get('rent_name')
#         rent_obj.phone_number1 = request.POST.get('phone1_name')
#         rent_obj.phone_number2 = request.POST.get('phone2_name')
#         rent_obj.email = request.POST.get('email_name')
#         rent_obj.number_of_members = request.POST.get('nfm_name')
#         rent_obj.nid_number = request.POST.get('nid_name')
#         rent_obj.user_name = request.POST.get('user_name')

#         data = (rent_obj.name,rent_obj.phone_number1,rent_obj.phone_number2,rent_obj.email,rent_obj.number_of_members,rent_obj.nid_number,rent_obj.user_name)
#         if data:
#               if len(rent_obj.phone_number1)!=11:
#                     messages.success(request, 'The phone number 1 must be 11')
#               elif len(rent_obj.phone_number2)!=11:
#                     messages.success(request, 'The phone number 2 must be 11')
#               elif Renter.objects.filter(name=rent_obj.user_name).exists():
#                     messages.success(request, 'This value already exists.')
#               else:

#                 rent_obj.save()
#                 messages.success(request, 'Data inserted successfully')
#         else:
#               messages.success(request, 'Required')
#         return redirect('home')

# def edit(request,id):
#       rent_obj = Renter.objects.get(id=id)
#       single_rent = {'cat_data':rent_obj,'id':id}
#       return render(request, 'admin/edit.html',single_rent)


# def update(request):
#         rent_obj = Renter()
#         rent_obj.name = request.POST.get('rent_name')
#         rent_obj.phone_number1 = request.POST.get('phone1_name')
#         rent_obj.phone_number2 = request.POST.get('phone2_name')
#         rent_obj.email = request.POST.get('email_name')
#         rent_obj.number_of_members = request.POST.get('nfm_name')
#         rent_obj.nid_number = request.POST.get('nid_name')
#         rent_obj.user_name = request.POST.get('user_name')

#         rent_obj.rent_id = request.POST.get('rent_id')

#         data = (rent_obj.name,rent_obj.phone_number1,rent_obj.phone_number2,rent_obj.email,rent_obj.number_of_members,rent_obj.nid_number,rent_obj.user_name)
#         if data:
#               if len(rent_obj.phone_number1)!=11:
#                     messages.success(request, 'The phone number 1 must be 11')
#               elif len(rent_obj.phone_number2)!=11:
#                     messages.success(request, 'The phone number 2 must be 11')
#               elif Renter.objects.filter(name=rent_obj.user_name).exists():
#                     messages.success(request, 'This value already exists.')
#               else:
#                   rent_obj= Renter.objects.get(id=rent_obj.rent_id)
#                   rent_obj.name =rent_obj.name
#                   rent_obj.phone_number1=rent_obj.phone_number1
#                   rent_obj.phone_number2=rent_obj.phone_number2
#                   rent_obj.email=rent_obj.email
#                   rent_obj.number_of_members=rent_obj.number_of_members
#                   rent_obj.nid_number=rent_obj.nid_number
#                   rent_obj.user_name=rent_obj.user_name

#                   rent_obj.save()
#                   messages.success(request, 'Data updated successfully')
#         else:
#               messages.success(request, 'Those fields cannot be empty')
#         return redirect('home')





# <td><a target="_blank" href="{% url 'edit_index' i.id %}">Edit </a><a>Delete</a></td>
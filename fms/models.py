from django.db import models

class Renter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=11)
    phone_number2 = models.CharField(max_length=11) 
    email = models.EmailField()
    number_of_members = models.CharField(max_length=15) 
    nid_number = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50, unique=True)





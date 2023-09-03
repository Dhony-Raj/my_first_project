from django.db import models

class Renter(models.Model):
    name = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15) 
    email = models.EmailField()
    number_of_members = models.PositiveIntegerField()
    nid_number = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

class userprofile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number1 = PhoneNumberField(blank=True, null=True)
    phone_number2 = PhoneNumberField(blank=True, null=True)
    number_of_members = models.IntegerField()
    nid_number = models.CharField(max_length=20)
    User = get_user_model()
    user_name = models.CharField(max_length=50, unique=True)
    user = User.objects.create_user(user_name, password='strong_password')

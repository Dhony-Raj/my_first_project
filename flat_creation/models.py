from django.db import models
from category.models import Category
from fms.models import Renter 

class Flat_create(models.Model):
    id = models.AutoField(primary_key=True)
    rent_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    flat_name = models.TextField(max_length=1000)
    flat_num = models.IntegerField()
    floor_num = models.IntegerField()
    nor_name = models.IntegerField() 
    room_size = models.IntegerField() 
    flat_price = models.IntegerField()
    flat_details = models.TextField(max_length=1000)
    flat_discount = models.IntegerField()
    room_pic = models.ImageField(null= True, blank=True, upload_to="images/")
    flat_discout_price = models.IntegerField(default=True)


# Create your models here.

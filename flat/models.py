from django.db import models
from fms.models import Renter

class Flat(models.Model):
    id = models.AutoField(primary_key=True)
    flat_num = models.IntegerField()
    floor_num = models.IntegerField()
    nor_name = models.IntegerField() 
    room_size = models.IntegerField() 
    flat_price = models.IntegerField()
    flat_after_discount = models.IntegerField()
    flat_details = models.TextField(max_length=1000)
    room_pic = models.ImageField(upload_to="images/")

# Create your models here.

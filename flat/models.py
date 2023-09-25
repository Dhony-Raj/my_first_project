from django.db import models

class Flat(models.Model):
    id = models.AutoField(primary_key=True)
    flat_num = models.IntegerField(max_length=100)
    floor_num = models.IntegerField(max_length=11)
    nor_name = models.IntegerField(max_length=11) 
    room_size = models.IntegerField(max_length=15) 
    flat_price = models.IntegerField(max_length=20)
    flat_dis = models.CharField(max_length=1000)
    room_pic = models.ImageField(max_length=1000)

# Create your models here.

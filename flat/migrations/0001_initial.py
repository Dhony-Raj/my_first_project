# Generated by Django 4.2.4 on 2023-10-11 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fms', '0003_remove_renter_password_alter_renter_phone_number1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flat_num', models.IntegerField(max_length=100)),
                ('floor_num', models.IntegerField(max_length=11)),
                ('nor_name', models.IntegerField(max_length=11)),
                ('room_size', models.IntegerField(max_length=15)),
                ('flat_price', models.IntegerField(max_length=20)),
                ('flat_discount', models.IntegerField(max_length=20)),
                ('flat_after_discount', models.IntegerField(max_length=20)),
                ('flat_details', models.TextField()),
                ('room_pic', models.ImageField(upload_to='images/')),
                ('renter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fms.renter')),
            ],
        ),
    ]
# Generated by Django 4.2.4 on 2023-10-21 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fms', '0003_remove_renter_password_alter_renter_phone_number1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat_create',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flat_num', models.IntegerField()),
                ('floor_num', models.IntegerField()),
                ('nor_name', models.IntegerField()),
                ('room_size', models.IntegerField()),
                ('flat_price', models.IntegerField()),
                ('flat_details', models.TextField(max_length=1000)),
                ('flat_discount', models.IntegerField()),
                ('room_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('rent_id_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fms.renter')),
            ],
        ),
    ]

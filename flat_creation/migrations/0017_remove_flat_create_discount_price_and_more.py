# Generated by Django 4.2.4 on 2023-10-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0016_remove_flat_create_flat_dis_flat_create_dis_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat_create',
            name='discount_price',
        ),
        migrations.AddField(
            model_name='flat_create',
            name='price_discount',
            field=models.IntegerField(default=True),
        ),
    ]

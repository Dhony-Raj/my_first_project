# Generated by Django 4.2.4 on 2023-10-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0005_flat_create_flat_discout_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat_create',
            name='flat_name',
            field=models.TextField(default=True, max_length=1000),
        ),
    ]

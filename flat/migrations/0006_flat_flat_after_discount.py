# Generated by Django 4.2.4 on 2023-10-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0005_remove_flat_flat_after_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='flat_after_discount',
            field=models.IntegerField(default=True),
        ),
    ]

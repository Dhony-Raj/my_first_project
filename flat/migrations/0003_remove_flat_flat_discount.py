# Generated by Django 4.2.4 on 2023-10-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0002_remove_flat_renter_id_alter_flat_flat_after_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='flat_discount',
        ),
    ]
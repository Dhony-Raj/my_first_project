# Generated by Django 4.2.4 on 2023-10-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0010_alter_flat_create_flat_discout_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat_create',
            old_name='flat_discout_price',
            new_name='flat_dis',
        ),
    ]
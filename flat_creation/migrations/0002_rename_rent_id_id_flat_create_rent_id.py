# Generated by Django 4.2.4 on 2023-10-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat_create',
            old_name='rent_id_id',
            new_name='rent_id',
        ),
    ]

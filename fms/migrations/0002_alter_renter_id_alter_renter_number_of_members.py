# Generated by Django 4.2.4 on 2023-09-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='renter',
            name='number_of_members',
            field=models.CharField(max_length=15),
        ),
    ]

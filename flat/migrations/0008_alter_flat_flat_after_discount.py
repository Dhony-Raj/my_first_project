# Generated by Django 4.2.4 on 2023-10-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0007_alter_flat_flat_after_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='flat_after_discount',
            field=models.IntegerField(blank=True),
        ),
    ]

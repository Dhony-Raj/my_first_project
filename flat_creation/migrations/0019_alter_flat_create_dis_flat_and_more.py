# Generated by Django 4.2.4 on 2023-11-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0018_alter_flat_create_dis_flat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_create',
            name='dis_flat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flat_create',
            name='price_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
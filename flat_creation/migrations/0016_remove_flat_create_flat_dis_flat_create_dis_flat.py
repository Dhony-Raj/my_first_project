# Generated by Django 4.2.4 on 2023-10-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat_creation', '0015_alter_flat_create_flat_dis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat_create',
            name='flat_dis',
        ),
        migrations.AddField(
            model_name='flat_create',
            name='dis_flat',
            field=models.IntegerField(default=True),
        ),
    ]

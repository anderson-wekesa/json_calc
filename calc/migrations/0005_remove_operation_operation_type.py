# Generated by Django 4.1.3 on 2022-11-03 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_opresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='operation_type',
        ),
    ]

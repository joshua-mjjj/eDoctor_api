# Generated by Django 3.2.8 on 2022-08-08 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20220808_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='balance',
        ),
    ]

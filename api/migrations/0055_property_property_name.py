# Generated by Django 3.2.8 on 2022-08-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_remove_property_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
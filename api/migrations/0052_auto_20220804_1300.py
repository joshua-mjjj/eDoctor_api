# Generated by Django 3.2.8 on 2022-08-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_auto_20220803_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_info',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='partial_payment',
            field=models.BooleanField(default=False),
        ),
    ]

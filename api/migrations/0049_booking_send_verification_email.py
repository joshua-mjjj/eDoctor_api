# Generated by Django 3.2.8 on 2022-07-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_booking_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='send_verification_email',
            field=models.BooleanField(default=False),
        ),
    ]
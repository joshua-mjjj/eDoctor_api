# Generated by Django 3.2.8 on 2022-08-08 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20220804_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_contact', models.CharField(max_length=100)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_email', models.CharField(blank=True, max_length=100, null=True)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Rental', 'Rental'), ('Hostel', 'Hostel'), ('Motel', 'Motel'), ('Retail Shop Space', 'Retail Shop Space')], max_length=52)),
                ('property_location', models.CharField(help_text='Where is the property located ?', max_length=152)),
                ('property_description', models.CharField(blank=True, max_length=200, null=True)),
                ('property_booked', models.BooleanField(default=False, help_text='Has the property been booked or taken ?')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False, help_text='Has the property been verified by admins ?')),
                ('send_property_verification_email', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('partial_payment', models.BooleanField(default=False, help_text='Do you accept partial/installments mode of payment ?')),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('additional_info', models.CharField(blank=True, help_text='Any more additional info or specifics about the property ?', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Client', 'Client')], max_length=32),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='property',
            name='verified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

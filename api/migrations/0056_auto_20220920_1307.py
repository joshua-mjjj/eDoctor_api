# Generated by Django 3.2.8 on 2022-09-20 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_property_property_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='contact',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hospital',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='patient_problem',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='speciality',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_sickness', models.CharField(blank=True, max_length=102, null=True)),
                ('description', models.CharField(blank=True, max_length=102, null=True)),
                ('symptoms', models.CharField(blank=True, max_length=102, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('verified_status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=52)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('pactient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
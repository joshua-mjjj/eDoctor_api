# Generated by Django 3.2.8 on 2021-12-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20211212_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='battallion_one',
            name='special_duty_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battallion_one',
            name='special_duty_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battallion_two',
            name='special_duty_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battallion_two',
            name='special_duty_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battallion_one',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Absent', 'Absent(AWOL)'), ('Transfered', 'Transfered'), ('Sick', 'Sick'), ('Dead', 'Dead'), ('Suspended', 'Suspended'), ('Dismissed', 'Dismissed'), ('In court', 'In court'), ('Deserted', 'Deserted'), ('On course', 'On course'), ('On mission', 'On mission'), ('On leave', 'On leave'), ('Interdiction', 'Interdiction'), ('Criminal court', 'Criminal court(remand / bail)'), ('Displinary court', 'Displinary court'), ('Special duty', 'Special duty'), ('On police course', 'On police course'), ('Undeployed', 'Undeployed')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Absent', 'Absent(AWOL)'), ('Transfered', 'Transfered'), ('Sick', 'Sick'), ('Dead', 'Dead'), ('Suspended', 'Suspended'), ('Dismissed', 'Dismissed'), ('In court', 'In court'), ('Deserted', 'Deserted'), ('On course', 'On course'), ('On mission', 'On mission'), ('On leave', 'On leave'), ('Interdiction', 'Interdiction'), ('Criminal court', 'Criminal court(remand / bail)'), ('Displinary court', 'Displinary court'), ('Special duty', 'Special duty'), ('On police course', 'On police course'), ('Undeployed', 'Undeployed')], max_length=32),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(default='Employee', max_length=40)),
                ('job_title', models.CharField(default='Job title', max_length=40)),
                ('sex', models.CharField(default='Sex', max_length=40)),
                ('department', models.CharField(default='Department', max_length=40)),
                ('email', models.CharField(default='email', max_length=40)),
                ('phone_number', models.CharField(default='Phone', max_length=12)),
                ('comment', models.CharField(default='Comment', max_length=100)),
            ],
        ),
    ]
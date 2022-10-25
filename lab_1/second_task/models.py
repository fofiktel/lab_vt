from django.db import models


class PersonalInformation(models.Model):
    employee_name = models.CharField(max_length=40,default='Employee')
    job_title = models.CharField(max_length=40,default='Job title')
    sex = models.CharField(max_length=40,default='Sex')
    department = models.CharField(max_length=40,default='Department')
    email = models.CharField(max_length=40,default='email')
    phone_number = models.CharField(max_length=12,default='Phone')
    comment = models.CharField(max_length=100,default='Comment')
# Create your models here.

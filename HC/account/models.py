from django.db import models
from django.contrib.auth.models import User
BLOOD_GROUPS= [
    ('1', 'O+'),
    ('2', 'O-'),
    ('3', 'A+'),
    ('4', 'A-'),
    ('5', 'B+'),
    ('6', 'B-'),
    ('7', 'AB+'),
    ('8', 'AB-'),
]
GENDER = [
    ('M','Male'),
    ('F','Female'),
]


class Patient(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    aadhar_no = models.IntegerField(primary_key=True, default=0)
    phone_no = models.IntegerField(default=0)
    password = models.CharField(max_length=100, default='123')
    conf_password = models.CharField(max_length=100, default='123')
    pincode = models.IntegerField(default=0)
    bgoup = models.CharField(max_length=1,choices=BLOOD_GROUPS,default='O+')
    gender = models.CharField(max_length=1,choices=GENDER,default='O+')

    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    aadharno = models.IntegerField(primary_key=True, default=0)
    phoneno = models.IntegerField(default=0)
    contactno = models.IntegerField(default=0)
    pincode = models.IntegerField(default=0)
    degree = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100, default='123')
    confirmpassword = models.CharField(max_length=100, default='123')

    def __str__(self):
        return self.firstname
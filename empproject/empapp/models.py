# Create your models here.
from django.db import models

class Contactus(models.Model):
    contact_name=models.CharField(max_length=100,blank=False)
    contact_emailid=models.EmailField(max_length=100,blank=False,unique=True)
    contact_sub=models.CharField(max_length=100,blank=False)
    contactno = models.BigIntegerField(blank=False,unique=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        db_table = "contactus_table"


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"


class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    #gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    #gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    #dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "registration_table"



class RecruiterRegistration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    #gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    #gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    #dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "recruiterregistration_table"



class Enroll(models.Model):
    name=models.CharField(max_length=100,blank=False)
    emailid=models.EmailField(max_length=100,blank=False,unique=True)
    contactno = models.BigIntegerField(blank=False,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "enroll_table"

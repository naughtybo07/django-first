from django.db import models



# Create your models here.
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class bank(models.Model):
    name = models.CharField(max_length=100)
    address=models.TextField(blank=True,null=True)
    emp_code=models.IntegerField(blank=True,null=True)
    phnum=models.BigIntegerField(blank=True,null=True)
    email=models.EmailField(default="unknown@gmail.com")
    joining_date=models.DateTimeField(default=timezone.now(),null=True,blank=True)
    password1 = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
    
class supplier(models.Model):
    name = models.CharField(max_length=100)
    address=models.TextField(blank=True,null=True)
    emp_code=models.IntegerField(blank=True,null=True)
    phnum=models.BigIntegerField(blank=True,null=True)
    email=models.EmailField(default="unknown@gmail.com")
    Credit_Ac_num=models.BigIntegerField(blank=True,null=True)
    credit_info=models.TextField(max_length=250)
    password1 = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=100)
    address=models.TextField(blank=True,null=True)
    phnum=models.BigIntegerField(blank=True,null=True)
    email=models.EmailField(default="unknown@gmail.com")
    loan_Ac_num=models.BigIntegerField(blank=True,null=True)
    loan_info=models.TextField(max_length=250)
    password1 = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
class request_invoice(models.Model):
    sup_code=models.IntegerField(blank=True,null=True)
    in_num= models.IntegerField(null=True,blank=True)
    in_date = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    in_amount = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)
    
class approve_invoice(models.Model):
    sup_code=models.IntegerField(blank=True,null=True)
    in_num= models.IntegerField(null=True,blank=True)
    in_date = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    in_amount = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)

class deny_invoice(models.Model):
    sup_code=models.IntegerField(blank=True,null=True)
    in_num= models.IntegerField(null=True,blank=True)
    in_date = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    in_amount = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)
    
class view_invoice(models.Model):
    sup_code=models.IntegerField(blank=True,null=True)
    in_num= models.IntegerField(null=True,blank=True)
    in_date = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    in_amount = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)

class upload_invoice(models.Model):
    sup_code=models.IntegerField(blank=True,null=True)
    in_num= models.IntegerField(null=True,blank=True)
    in_date = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    in_amount = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)
    
from django.db import models

# Create your models here.
class contact(models.Model):
    fname=models.CharField(max_length=100,null= True)
    lname=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    message=models.TextField(null=True)

class vehicle(models.Model):
    vehicleimage=models.ImageField(upload_to='static/Vehicle/',null=True)
    rent=models.IntegerField(null=True)
    vehicle1=models.CharField(max_length=100,null=True)
    vehicle2= models.CharField(max_length=100, null=True)
    vehicle3= models.CharField(max_length=100, null=True)

class ourservice(models.Model):
    heading=models.CharField(max_length=100,null=True)
    des=models.TextField(null=True)

class testimonials(models.Model):
    desc=models.TextField(null=True)
    picture=models.ImageField(upload_to='static/testimonials/',null=True)
    name=models.CharField(max_length=100,null=True)

from django.shortcuts import render
from  .models import  *
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method=="GET":
        fname=request.GET.get('fname')
        lname=request.GET.get('lname')
        email=request.GET.get('email')
        message=request.GET.get('message')
        contact(fname=fname,lname=lname,email=email,message=message).save()
    vehicledata=vehicle.objects.all().order_by('-id')[0:3]
    ourservicedata=ourservice.objects.all().order_by('-id')[0:4]
    testimonialsdata=testimonials.objects.all().order_by('-id')[0:4]
    md={
        "data":"Aman Tiwari",
        "vehicle":vehicledata,
        "ourservice":ourservicedata,
        "testimonials":testimonialsdata,
    }
    return render(request,'home.html',md)

def demo(request):
    return  render(request,'demo.html')
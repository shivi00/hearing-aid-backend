from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.middleware import csrf
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.


@csrf_exempt
def details(request):

    if request.method=='POST': 
        print(request.body)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user = Appointment.objects.create( name=name,email=email,message=message)
        user.save()
    return HttpResponse({"message":'Successful'})


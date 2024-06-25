from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def phone(request):
    return render(request, 'pages/phone.html')

def computer(request):
    return render(request, 'pages/computer.html')

def tablet(request):
    return render(request, 'pages/tablet.html')

def accesory(request):
    return render(request, 'pages/accesory.html')

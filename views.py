from django.http import HttpResponse
from django.shortcuts import render

def Home(req):
    return render(req, 'home.html')

def Login(req):
    return render(req, 'login.html')
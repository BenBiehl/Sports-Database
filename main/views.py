from django.http import HttpResponse
from django.shortcuts import render

from .models import User

loggedIn = False

def landing_page(request):
    return render(request, "main/landing_page.html")

def login_page(request):
    return render(request, "main/login_page.html")

def signup_page(request):
    return render(request, "main/signup_page.html")
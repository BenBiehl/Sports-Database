from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import User

loggedIn = False

def landing_page(request):
    return render(request, "main/landing_page.html")

def login_page(request):
    return render(request, "main/login_page.html")

def signup_page(request):
    return render(request, "main/signup_page.html")

def user_page(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "main/user_page.html", {"user": user})
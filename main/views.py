from django.http import HttpResponse
from django.shortcuts import render

from .models import User

def landing_page(request):
    return render(request, "main/landingpage.html")
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F

from .models import User, GlobalStats
from .forms import SignupForm

loggedIn = False

def landing_page(request):
    return render(request, "main/landing_page.html")

def login_page(request):
    return render(request, "main/login_page.html")

def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]
            new_user = User(userName = user_name, passWord = password)
            new_user.save()
            GlobalStats.objects.filter(id=1).update(numUsers=F('numUsers') + 1)
    else:
        form = SignupForm()

    return render(request, "main/signup_page.html", {"form": form})

def user_page(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    return render(request, "main/user_page.html", {"user": user})
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib import messages

from .models import User, GlobalStat, Athlete, BaseballStat, BasketballStat, FootballStat, SoccerStat
from .forms import LogSignForm, ProfileForm

def landing_page(request):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name
    }

    return render(request, "main/landing_page.html", context)

def login_page(request):
    invalid_user = False
    invalid_password = False
    invalid_info = False

    if request.method == "POST":
        form = LogSignForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]
            if User.objects.filter(userName=user_name).exists():
                if User.objects.filter(userName=user_name, passWord=password).exists():
                    request.session['logged_in'] = True
                    request.session['curr_user_name'] = user_name
                    return redirect('landing_page')
                else:
                    invalid_password = True
                    form = LogSignForm()
            else:
                invalid_user = True
                form = LogSignForm()
        else:
            invalid_info = True
            form = LogSignForm()
    else:
        form = LogSignForm()

    context = {
        "form": form,
        "invalid_user": invalid_user,
        "invalid_password": invalid_password,
        "invalid_info": invalid_info
    }

    return render(request, "main/login_page.html", context)

def logout(request):
    request.session.flush()
    return redirect('landing_page')

def signup_page(request):
    user_taken = False
    invalid_info = False

    if request.method == "POST":
        form = LogSignForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]
            if User.objects.filter(userName=user_name).exists():
                user_taken = True
                form = LogSignForm()
            else:
                new_user = User(userName = user_name, passWord = password)
                new_user.save()
                GlobalStat.objects.filter(id=1).update(numUsers=F('numUsers') + 1)
                request.session['logged_in'] = True
                request.session['curr_user_name'] = user_name
                return redirect('landing_page')
        else:
            invalid_info = True
            form = LogSignForm()
    else:
        form = LogSignForm()
    
    context = {
        "form": form,
        "user_taken": user_taken,
        "invalid_info": invalid_info
    }

    return render(request, "main/signup_page.html", context)

def user_page(request, user_name):
    user = get_object_or_404(User, pk=user_name)
    invalid_info = False
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            favorite_team = form.cleaned_data["fav_team"]
            user.teamName = favorite_team
            user.save()
        else:
            form = ProfileForm()
            invalid_info = True
    else:
        form = ProfileForm()

    context = {
        "user": user,
        "form": form,
        "invalid_info": invalid_info
    }

    return render(request, "main/user_page.html", context)

def sports_page(request, sport):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
    is_admin = False

    if logged_in and curr_user_name:
        try:
            user = User.objects.get(userName=curr_user_name)
            is_admin = user.isAdmin
        except User.DoesNotExist:
            is_admin = False

    if sport == "baseball":
        stats = BaseballStat.objects.select_related('athlete').all()
    elif sport == "basketball":
        stats = BasketballStat.objects.select_related('athlete').all()
    elif sport == "soccer":
        stats = SoccerStat.objects.select_related('athlete').all()
    else:
        stats = FootballStat.objects.select_related('athlete').all()

    if stats:
        are_stats = True
    else:
        are_stats = False

    context = {
        "logged_in": logged_in,
        "is_admin": is_admin,
        "are_stats": are_stats,
        "sport": sport,
        "stats": stats
    }

    return render(request, "main/sports_page.html", context)

def add_athlete(request, sport):
    context = {"sport": sport}
    return render(request, "main/add_athlete.html", context)

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib import messages

from .models import User, GlobalStat, Athlete, BaseballStat, BasketballStat, FootballStat, SoccerStat
from .forms import LogSignForm, ProfileForm, AddAthleteForm, BaseballForm, BasketballForm, SoccerForm, FootballForm

# Page Request Functions
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
    header = table_header(sport)

    if logged_in and curr_user_name:
        try:
            user = User.objects.get(userName=curr_user_name)
            is_admin = user.isAdmin
        except User.DoesNotExist:
            is_admin = False

    stats = get_sports_stats(sport)

    if stats:
        are_stats = True
    else:
        are_stats = False

    context = {
        "logged_in": logged_in,
        "is_admin": is_admin,
        "are_stats": are_stats,
        "sport": sport,
        "stats": stats,
        "header": header
    }

    return render(request, "main/sports_page.html", context)

def add_athlete(request, sport):
    athlete_form = AddAthleteForm(request.POST or None)
    sport_form = None

    if sport == "baseball":
        sport_form = BaseballForm(request.POST or None)
    elif sport == "basketball":
        sport_form = BasketballForm(request.POST or None)
    elif sport == "soccer":
        sport_form = SoccerForm(request.POST or None)
    else:
        sport_form = FootballForm(request.POST or None)

    if request.method == "POST" and athlete_form.is_valid() and sport_form and sport_form.is_valid():
        athlete = Athlete(
            firstName=athlete_form.cleaned_data['first_name'],
            lastName=athlete_form.cleaned_data['last_name'],
            teamName=athlete_form.cleaned_data['team_name'],
            sport=sport.capitalize()
        )
        athlete.save()

        if sport == "baseball":
            BaseballStat.objects.create(
                athlete=athlete,
                battingAvg=sport_form.cleaned_data['batting_avg'],
                homeRuns=sport_form.cleaned_data['home_runs'],
                era=sport_form.cleaned_data['era'],
                rbi=sport_form.cleaned_data['rbi'],
                stolenBases=sport_form.cleaned_data['stolen_bases']
            )
        elif sport == "basketball":
            BasketballStat.objects.create(
                athlete=athlete,
                pointsPG=sport_form.cleaned_data['points_pg'],
                assistsPG=sport_form.cleaned_data['assists_pg'],
                reboundsPG=sport_form.cleaned_data['rebounds_pg'],
                threePPerc=sport_form.cleaned_data['threepoint_perc'],
                freeThrowPerc=sport_form.cleaned_data['freethrow_perc']
            )
        elif sport == "soccer":
            SoccerStat.objects.create(
                athlete=athlete,
                goalsScored=sport_form.cleaned_data['goals_scored'],
                shots=sport_form.cleaned_data['shots'],
                saves=sport_form.cleaned_data['saves'],
                fouls=sport_form.cleaned_data['fouls'],
                minutesPlayed=sport_form.cleaned_data['minutes_played']
            )
        else:
            FootballStat.objects.create(
                athlete=athlete,
                passingYards=sport_form.cleaned_data['passing_yards'],
                rushingYards=sport_form.cleaned_data['rushing_yards'],
                tackles=sport_form.cleaned_data['tackles'],
                sacks=sport_form.cleaned_data['sacks'],
                interceptions=sport_form.cleaned_data['interceptions']
            )

        return redirect('sports_page', sport)

    # Context setup for GET request or form errors
    context = {
        "sport": sport,
        "athlete_form": athlete_form,
        "sport_form": sport_form,
    }

    return render(request, "main/add_athlete.html", context)

# Other Functions
def get_sports_stats(sport):
    if sport == "baseball":
        stats = BaseballStat.objects.select_related('athlete').all()
    elif sport == "basketball":
        stats = BasketballStat.objects.select_related('athlete').all()
    elif sport == "soccer":
        stats = SoccerStat.objects.select_related('athlete').all()
    else:
        stats = FootballStat.objects.select_related('athlete').all()
    return stats

def table_header(sport):
    if sport == "baseball":
        header = ['Name', 'Batting Avg', 'Home Runs', 'ERA', 'RBI', 'Stolen Bases']
    elif sport == "basketball":
        header = ['Name', 'Points PG', 'Assists PG', 'Rebounds PG', 'Three Point %', 'Three Throw %']
    elif sport == "soccer":
        header = ['Name', 'Goals', 'Shots', 'Saves', 'Fouls', 'Minutes Played']
    else:
        header = ['Name', 'Passing Yards', 'Rushing Yards', 'Tackles', 'Sacks', 'Interceptions']
    return header
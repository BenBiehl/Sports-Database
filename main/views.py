from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib import messages

from .models import User, GlobalStat, Athlete, BaseballStat, BasketballStat, FootballStat, SoccerStat
from .forms import LogSignForm, ProfileForm, AddAthleteForm, BaseballForm, BasketballForm, SoccerForm, FootballForm, EditAthleteForm, AthleteSearchForm

# Page Request Functions
def landing_page(request):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
    
    viewed_athletes = Athlete.objects.order_by("-numViews")[:5]

    search_form = AthleteSearchForm(request.GET or None)
    
    search_results = []
    if search_form.is_valid():
        query = search_form.cleaned_data.get('search_query')
        if query:
            # Search by first name or last name, case insensitive
            search_results = Athlete.objects.filter(
                firstName__icontains=query
            ) | Athlete.objects.filter(
                lastName__icontains=query
            )

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name,
        "viewed_athletes": viewed_athletes,
        "search_form": search_form,
        "search_results": search_results
    }

    return render(request, "main/landing_page.html", context)

def search_page(request):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
    search_query = request.GET.get('search_query', '')
    
    search_form = AthleteSearchForm(request.GET or None)
    
    search_results = []
    if search_form.is_valid():
        query = search_form.cleaned_data.get('search_query')
        if query:
            # Search by first name or last name, case insensitive
            search_results = Athlete.objects.filter(
                firstName__icontains=query
            ) | Athlete.objects.filter(
                lastName__icontains=query
            )

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name,
        "search_form": search_form,
        "search_results": search_results
    }
    return render(request, 'main/search_page.html', context)

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
    sort_num = request.GET.get('sort_num', 0)
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

    stats = get_sorted_sports_stats(sport, int(sort_num))

    are_stats = bool(stats)

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name,
        "is_admin": is_admin,
        "are_stats": are_stats,
        "sport": sport,
        "stats": stats,
        "header": header
    }

    return render(request, "main/sports_page.html", context)


def add_athlete(request, sport):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
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
            firstName=athlete_form.cleaned_data['firstName'],
            lastName=athlete_form.cleaned_data['lastName'],
            teamName=athlete_form.cleaned_data['teamName'],
            sport=sport.capitalize()
        )
        athlete.save()

        if sport == "baseball":
            BaseballStat.objects.create(
                athlete=athlete,
                battingAvg=sport_form.cleaned_data['battingAvg'],
                homeRuns=sport_form.cleaned_data['homeRuns'],
                era=sport_form.cleaned_data['era'],
                rbi=sport_form.cleaned_data['rbi'],
                stolenBases=sport_form.cleaned_data['stolenBases']
            )
        elif sport == "basketball":
            BasketballStat.objects.create(
                athlete=athlete,
                pointsPG=sport_form.cleaned_data['pointsPG'],
                assistsPG=sport_form.cleaned_data['assistsPG'],
                reboundsPG=sport_form.cleaned_data['reboundsPG'],
                threePPerc=sport_form.cleaned_data['threePPerc'],
                freeThrowPerc=sport_form.cleaned_data['freeThrowPerc']
            )
        elif sport == "soccer":
            SoccerStat.objects.create(
                athlete=athlete,
                goalsScored=sport_form.cleaned_data['goalsScored'],
                shots=sport_form.cleaned_data['shots'],
                saves=sport_form.cleaned_data['saves'],
                fouls=sport_form.cleaned_data['fouls'],
                minutesPlayed=sport_form.cleaned_data['minutesPlayed']
            )
        else:
            FootballStat.objects.create(
                athlete=athlete,
                passingYards=sport_form.cleaned_data['passingYards'],
                rushingYards=sport_form.cleaned_data['rushingYards'],
                tackles=sport_form.cleaned_data['tackles'],
                sacks=sport_form.cleaned_data['sacks'],
                interceptions=sport_form.cleaned_data['interceptions']
            )

        return redirect('sports_page', sport)

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name,
        "sport": sport,
        "athlete_form": athlete_form,
        "sport_form": sport_form,
    }

    return render(request, "main/add_athlete.html", context)

def athlete_page(request, sport, athlete_id):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
    is_admin = False

    if logged_in and curr_user_name:
        try:
            user = User.objects.get(userName=curr_user_name)
            is_admin = user.isAdmin
        except User.DoesNotExist:
            is_admin = False

    athlete_id = int(athlete_id)
    athlete = Athlete.objects.filter(id=athlete_id).first()
    athlete.numViews += 1
    athlete.save(update_fields=['numViews'])

    athlete_stats = None
    if sport == 'baseball':
        athlete_stats = get_object_or_404(BaseballStat, athlete=athlete)
    elif sport == 'basketball':
        athlete_stats = get_object_or_404(BasketballStat, athlete=athlete)
    elif sport == 'soccer':
        athlete_stats = get_object_or_404(SoccerStat, athlete=athlete)
    elif sport == 'football':
        athlete_stats = get_object_or_404(FootballStat, athlete=athlete)

    context = {
        "athlete": athlete,
        "athlete_stats": athlete_stats,
        "is_admin": is_admin,
        "sport": sport,
        "logged_in": logged_in,
        "curr_user_name": curr_user_name
    }

    return render(request, "main/athlete_page.html", context)

def edit_athlete(request, sport, athlete_id):
    logged_in = request.session.get('logged_in', False)
    curr_user_name = request.session.get('curr_user_name', "")
    athlete = get_object_or_404(Athlete, id=athlete_id)
    
    athlete_form = EditAthleteForm(request.POST or None, instance=athlete)
    
    if sport == "baseball":
        sport_stat = get_object_or_404(BaseballStat, athlete=athlete)
        sport_form = BaseballForm(request.POST or None, instance=sport_stat)
    elif sport == "basketball":
        sport_stat = get_object_or_404(BasketballStat, athlete=athlete)
        sport_form = BasketballForm(request.POST or None, instance=sport_stat)
    elif sport == "soccer":
        sport_stat = get_object_or_404(SoccerStat, athlete=athlete)
        sport_form = SoccerForm(request.POST or None, instance=sport_stat)
    else:
        sport_stat = get_object_or_404(FootballStat, athlete=athlete)
        sport_form = FootballForm(request.POST or None, instance=sport_stat)

    if request.method == "POST":
        if athlete_form.is_valid() and sport_form.is_valid():
            athlete_form.save()
            sport_form.save()

    context = {
        "logged_in": logged_in,
        "curr_user_name": curr_user_name,
        "sport": sport,
        "athlete_form": athlete_form,
        "sport_form": sport_form,
    }

    return render(request, "main/edit_athlete.html", context)

# Other Functions
def get_sorted_sports_stats(sport, sort_num=0):
    stats = None
    
    if sport == "baseball":
        stats = BaseballStat.objects.select_related('athlete').all()
        match sort_num:
            case 1:
                stats = stats.order_by('athlete__firstName')
            case 2:
                stats = stats.order_by('-battingAvg')
            case 3:
                stats = stats.order_by('-homeRuns')
            case 4:
                stats = stats.order_by('-era')
            case 5:
                stats = stats.order_by('-rbi')
            case 6:
                stats = stats.order_by('-stolenBases')
                
    elif sport == "basketball":
        stats = BasketballStat.objects.select_related('athlete').all()
        match sort_num:
            case 1:
                stats = stats.order_by('athlete__firstName')
            case 2:
                stats = stats.order_by('-pointsPG')
            case 3:
                stats = stats.order_by('-assistsPG')
            case 4:
                stats = stats.order_by('-reboundsPG')
            case 5:
                stats = stats.order_by('-threePPerc')
            case 6:
                stats = stats.order_by('-freeThrowPerc')
                
    elif sport == "soccer":
        stats = SoccerStat.objects.select_related('athlete').all()
        match sort_num:
            case 1:
                stats = stats.order_by('athlete__firstName')
            case 2:
                stats = stats.order_by('-goalsScored')
            case 3:
                stats = stats.order_by('-shots')
            case 4:
                stats = stats.order_by('-saves')
            case 5:
                stats = stats.order_by('-fouls')
            case 6:
                stats = stats.order_by('-minutesPlayed')
                
    elif sport == "football":
        stats = FootballStat.objects.select_related('athlete').all()
        match sort_num:
            case 1:
                stats = stats.order_by('athlete__firstName')
            case 2:
                stats = stats.order_by('-passingYards')
            case 3:
                stats = stats.order_by('-rushingYards')
            case 4:
                stats = stats.order_by('-tackles')
            case 5:
                stats = stats.order_by('-sacks')
            case 6:
                stats = stats.order_by('-interceptions')
    return stats


def table_header(sport):
    if sport == "baseball":
        header = ['Name', 'Batting Avg', 'Home Runs', 'ERA', 'RBI', 'Stolen Bases']
    elif sport == "basketball":
        header = ['Name', 'Points PG', 'Assists PG', 'Rebounds PG', 'Three Point %', 'Free Throw %']
    elif sport == "soccer":
        header = ['Name', 'Goals', 'Shots', 'Saves', 'Fouls', 'Minutes Played']
    else:
        header = ['Name', 'Passing Yards', 'Rushing Yards', 'Tackles', 'Sacks', 'Interceptions']
    return header
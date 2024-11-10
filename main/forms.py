from django import forms
from django.forms import TextInput

class LogSignForm(forms.Form):
    user_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 200px;'})
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 200px;'})
    )

class ProfileForm(forms.Form):
    fav_team = forms.CharField(
        label="Add/Change Team",
        max_length=20
    )

class AddAthleteForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 200px;'})
    )
    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 200px;'})
    )
    team_name = first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Team Name', 'style': 'width: 200px;'})
    )

class BaseballForm(forms.Form):
    batting_avg = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Batting Avg', 'style': 'width: 200px;'})
    )
    home_runs = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Home Runs', 'style': 'width: 200px;'})
    )
    era = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'ERA', 'style': 'width: 200px;'})
    )
    rbi = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'RBI', 'style': 'width: 200px;'})
    )
    stolen_bases = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Stolen Bases', 'style': 'width: 200px;'})
    )

class BasketballForm(forms.Form):
    points_pg = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'Points PG', 'style': 'width: 200px;'})
    )
    assists_pg = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'Assists PG', 'style': 'width: 200px;'})
    )
    rebounds_pg = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'Rebounds PG', 'style': 'width: 200px;'})
    )
    threepoint_perc = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'Three Point %', 'style': 'width: 200px;'})
    )
    freethrow_perc = forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder': 'Free Throw %', 'style': 'width: 200px;'})
    )

class SoccerForm(forms.Form):
    goals_scored = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Goals Scored', 'style': 'width: 200px;'})
    )
    shots = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Shots', 'style': 'width: 200px;'})
    )
    saves = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Saves', 'style': 'width: 200px;'})
    )
    fouls = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Fouls', 'style': 'width: 200px;'})
    )
    minutes_played = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Minutes Played', 'style': 'width: 200px;'})
    )

class FootballForm(forms.Form):
    passing_yards = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Passing Yards', 'style': 'width: 200px;'})
    )
    rushing_yards = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Rushing Yards', 'style': 'width: 200px;'})
    )
    tackles = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Tackles', 'style': 'width: 200px;'})
    )
    sacks = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Sacks', 'style': 'width: 200px;'})
    )
    interceptions = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Interceptions', 'style': 'width: 200px;'})
    )
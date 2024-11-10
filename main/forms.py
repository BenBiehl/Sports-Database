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
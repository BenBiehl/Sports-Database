from django import forms
from .models import Athlete, BaseballStat, BasketballStat, SoccerStat, FootballStat

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

class AddAthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['firstName', 'lastName', 'teamName']
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 200px;'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 200px;'}),
            'teamName': forms.TextInput(attrs={'placeholder': 'Team Name', 'style': 'width: 200px;'}),
        }

class BaseballForm(forms.ModelForm):
    class Meta:
        model = BaseballStat
        fields = ['battingAvg', 'homeRuns', 'era', 'rbi', 'stolenBases']
        widgets = {
            'battingAvg': forms.TextInput(attrs={'placeholder': 'Batting Avg', 'style': 'width: 200px;'}),
            'homeRuns': forms.TextInput(attrs={'placeholder': 'Home Runs', 'style': 'width: 200px;'}),
            'era': forms.TextInput(attrs={'placeholder': 'ERA', 'style': 'width: 200px;'}),
            'rbi': forms.TextInput(attrs={'placeholder': 'RBI', 'style': 'width: 200px;'}),
            'stolenBases': forms.TextInput(attrs={'placeholder': 'Stolen Bases', 'style': 'width: 200px;'}),
        }

class BasketballForm(forms.ModelForm):
    class Meta:
        model = BasketballStat
        fields = ['pointsPG', 'assistsPG', 'reboundsPG', 'threePPerc', 'freeThrowPerc']
        widgets = {
            'pointsPG': forms.TextInput(attrs={'placeholder': 'Points PG', 'style': 'width: 200px;'}),
            'assistsPG': forms.TextInput(attrs={'placeholder': 'Assists PG', 'style': 'width: 200px;'}),
            'reboundsPG': forms.TextInput(attrs={'placeholder': 'Rebounds PG', 'style': 'width: 200px;'}),
            'threePPerc': forms.TextInput(attrs={'placeholder': 'Three Point %', 'style': 'width: 200px;'}),
            'freeThrowPerc': forms.TextInput(attrs={'placeholder': 'Free Throw %', 'style': 'width: 200px;'}),
        }

class SoccerForm(forms.ModelForm):
    class Meta:
        model = SoccerStat
        fields = ['goalsScored', 'shots', 'saves', 'fouls', 'minutesPlayed']
        widgets = {
            'goalsScored': forms.TextInput(attrs={'placeholder': 'Goals Scored', 'style': 'width: 200px;'}),
            'shots': forms.TextInput(attrs={'placeholder': 'Shots', 'style': 'width: 200px;'}),
            'saves': forms.TextInput(attrs={'placeholder': 'Saves', 'style': 'width: 200px;'}),
            'fouls': forms.TextInput(attrs={'placeholder': 'Fouls', 'style': 'width: 200px;'}),
            'minutesPlayed': forms.TextInput(attrs={'placeholder': 'Minutes Played', 'style': 'width: 200px;'}),
        }

class FootballForm(forms.ModelForm):
    class Meta:
        model = FootballStat
        fields = ['passingYards', 'rushingYards', 'tackles', 'sacks', 'interceptions']
        widgets = {
            'passingYards': forms.TextInput(attrs={'placeholder': 'Passing Yards', 'style': 'width: 200px;'}),
            'rushingYards': forms.TextInput(attrs={'placeholder': 'Rushing Yards', 'style': 'width: 200px;'}),
            'tackles': forms.TextInput(attrs={'placeholder': 'Tackles', 'style': 'width: 200px;'}),
            'sacks': forms.TextInput(attrs={'placeholder': 'Sacks', 'style': 'width: 200px;'}),
            'interceptions': forms.TextInput(attrs={'placeholder': 'Interceptions', 'style': 'width: 200px;'}),
        }

class EditAthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['firstName', 'lastName', 'height', 'weight', 'age', 'wins', 'losses', 'joinYear', 'teamName', 'position', 'gamesPlayed']
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 200px;'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 200px;'}),
            'teamName': forms.TextInput(attrs={'placeholder': 'Team Name', 'style': 'width: 200px;'}),
            'position': forms.TextInput(attrs={'placeholder': 'Position', 'style': 'width: 200px;'}),
            'height': forms.TextInput(attrs={'placeholder': 'Height', 'style': 'width: 200px;'}),
            'weight': forms.TextInput(attrs={'placeholder': 'Weight', 'style': 'width: 200px;'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age', 'style': 'width: 200px;'}),
            'wins': forms.NumberInput(attrs={'placeholder': 'Wins', 'style': 'width: 200px;'}),
            'losses': forms.NumberInput(attrs={'placeholder': 'Losses', 'style': 'width: 200px;'}),
            'joinYear': forms.NumberInput(attrs={'placeholder': 'Join Year', 'style': 'width: 200px;'}),
            'gamesPlayed': forms.NumberInput(attrs={'placeholder': 'Games Played', 'style': 'width: 200px;'})
        }

class AthleteSearchForm(forms.Form):
    search_query = forms.CharField(label="Search Athletes", max_length=100, required=False)
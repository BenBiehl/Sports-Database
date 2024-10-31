from django import forms
from django.forms import TextInput

class LogSignForm(forms.Form):
    user_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 200px;'}))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 200px;'}))

class ProfileForm(forms.Form):
    fav_team = forms.CharField(label="Add/Change Team", max_length=20)
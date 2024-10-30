from django import forms

class LogSignForm(forms.Form):
    user_name = forms.CharField(label="User Name:", max_length=20)
    password = forms.CharField(label="Password:", max_length=20)

class ProfileForm(forms.Form):
    fav_team = forms.CharField(label="Add/Change Team", max_length=20)
from django import forms

class SignupForm(forms.Form):
    user_name = forms.CharField(label="User Name:", max_length=20)
    password = forms.CharField(label="Password:", max_length=20)
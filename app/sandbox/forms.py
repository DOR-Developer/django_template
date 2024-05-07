from django import forms

class LoginForm(forms.Form):
    # TODO : Add form validation and custom fields.
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class SignupForm(forms.Form):
    # TODO : Add form validation and custom fields.
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    repassword = forms.CharField(label="Repeat password", widget=forms.PasswordInput())
    terms = forms.BooleanField(label="I've read and accept the terms and conditions.")
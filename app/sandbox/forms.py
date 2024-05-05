from django import forms

class LoginForm:
    # TODO : Add form validation and custom fields.
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    pass

class SignupForm:
    # TODO : Add form validation and custom fields.
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repassword = forms.CharField(widget=forms.PasswordInput())
    terms = forms.BooleanField()
    pass
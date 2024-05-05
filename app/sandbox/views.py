from django.shortcuts import render

from django.conf import settings

# Create your views here.
def home_view(request):

    # TODO : Access database using settings.
    print(settings.DATABASE_URL)

    return render(request, "home.html")


def login_view(request):

    return render(request, "login.html")

def signup_view(request):
    
    return render(request, "signup.html")
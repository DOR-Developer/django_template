from django.shortcuts import render

from django.conf import settings
from .forms import LoginForm, SignupForm

# Create your views here.
def home_view(request):

    # TODO : Access database using settings.
    print(settings.DATABASE_URL)

    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
    else:
        form = SignupForm()
    
    return render(request, "signup.html", {"form": form})
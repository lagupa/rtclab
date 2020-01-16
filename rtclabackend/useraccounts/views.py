from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from equipment.views import equipment

# Create your views here.


def user_view(request):
    if not request.user.is_authenticated:
        return render(request, "useraccounts/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "useraccounts/user.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('equipment')
    else:
        return render(request, "useraccounts/login.html", {"message": 'Invalid Credentials'})


def logout_view(request):
    print('logout successfully...')
    logout(request)
    print('logout successfully')
    return render(request, "useraccounts/login.html", {"message": "You are now logged out <br> "})


def register(request):
    if request.POST:
        user_name = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            user = User.objects.create_user(
                username=user_name, email=email, password=password1)
            if last_name and first_name:
                user.first_name = first_name
                user.last_name = last_name
            user.save()
            return render(request, "useraccounts/login.html", {"message": 'Account successfully created! You can now login...'})
        else:
            print(user_name, email, first_name,
                  last_name, password1, password2)
            user_name = user_name
            context = {
                "message": "Passwords didn't match!"
            }
            return render(request, "useraccounts/register.html", context)
    else:
        return render(request, "useraccounts/register.html", {"message": "EXECELLENT!"})

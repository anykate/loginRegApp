from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request, 'loginRegApp/index.html', {})


def createuser(request):
    # print(request.POST)
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    password = request.POST['pwd']

    # newuser = User.objects.create(
    #     first_name=first_name,
    #     last_name=last_name,
    #     email=email,
    #     password=make_password(password) # Never save password(s) as plain text
    # )

    return redirect('loginRegApp:success')


def success(request):
    return render(request, 'loginRegApp/success.html', {})

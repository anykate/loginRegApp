from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'loginRegApp/index.html', {})


def createuser(request):
    print(request.POST)
    return redirect('loginRegApp:success')


def success(request):
    return render(request, 'loginRegApp/success.html', {})

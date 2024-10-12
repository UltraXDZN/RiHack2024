from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def news_view(request):
    return render(request, 'news.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')

def citySelection_view(request):
    return render(request, "calendar.html")

from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')


def news_view(request):
    if request.user.is_authenticated:
        return render(request, 'news.html')
    else:
        return redirect('/login')


def calendar_view(request):
    if request.user.is_authenticated:
        return render(request, 'calendar.html')
    else:
        return redirect('/login')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')

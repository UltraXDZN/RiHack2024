from django.shortcuts import render, redirect, get_object_or_404

from news.models import NewsFull


def home_view(request):
    return render(request, "home.html")


def news_view(request):
    if request.user.is_authenticated:
        return render(request, "news.html")
    else:
        return redirect("/login")

def news_detail(request, id):
    article = get_object_or_404(NewsFull, id=id)
    return render(request, 'news_detail.html', {'article': article})


def calendar_view(request):
    if request.user.is_authenticated:
        return render(request, "calendar.html")
    else:
        return redirect("/login")


def login_view(request):
    return render(request, "login.html")


def citySelection_view(request):
    return render(request, "citySelection.html")


def register_view(request):
    return render(request, "register.html")



def market_view(request):
    return render(request, "market.html")


def profile_view(request):
    return render(request, "profile.html")


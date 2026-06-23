from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    context = {
        "name": "Lux",
        "age": 16,
        "city": "Derbent"
    }
    return render(request, "hello.html", context)


def about(request):
    return HttpResponse("Это мой первый Django проект")


def contacts(request):
    return HttpResponse("Мои контакты: TG:@Luxxxov")


def news(request):
    context = {
        "news": ["Новость левая", "Новость центральная", "Новость правая"]
    }
    return render(request, "news.html", context)


def products(request):
    context = {
        "products" : ["VPN Basic", "VPN Pro", "VPN Ultra"]
    }
    return render(request, "products.html", context)


def users(request):
    context = {
        "name": "NAME",
        "age": 18
    }
    return render(request, "user.html", context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from game.models import Product, Subscription


def delete_product(request, id):

    product = Product.objects.get(id=id)
    product.delete()

    return redirect("/products/")


def hello(request):
    context = {
        "name": "Lux",
        "age": 16,
        "city": "Derbent"
    }
    return render(request, "hello.html", context)


def about(request):
    return render(request, "about.html")


def contacts(request):
    return HttpResponse("Мои контакты: TG:@Luxxxov")


def news(request):
    context = {
        "news": ["Новость левая", "Новость центральная", "Новость правая"]
    }
    return render(request, "news.html", context)


def products(request):

    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })


def users(request):
    users = [
    "Lux",
    "Kate",
    "Alex"
    ]
    
    return render(request, "users.html")


def subscriptions(request):
    subscriptions = Subscription.objects.all()
    return render(request, "subscriptions.html", {
        "subscriptions": subscriptions
    })


def create_subscription(request):
    if request.method == "POST":

        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")

        Subscription.objects.create(
        name=name,
        price=price,
        description=description
        )
        
        return redirect("/subscriptions/")
    
    return render(request, "create_subscription.html")


def edit_subscription(request, id):

    subscription = Subscription.objects.get(id=id)

    if request.method == "POST":

        subscription.name = request.POST.get("name")
        subscription.price = request.POST.get("price")
        subscription.description = request.POST.get("description")

        subscription.save()

        return redirect("/subscriptions/")

    return render(
        request,
        "edit_subscription.html",
        {
            "subscription": subscription
        }
    )   
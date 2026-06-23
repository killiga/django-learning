from django.shortcuts import render, redirect
from django.http import HttpResponse
from game.models import Product


def delete_product(request, id):

    product = Product.objects.get(id=id)
    product.delete()

    return redirect("/products/")


def edit_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":

        product.name = request.POST.get("name")
        product.price = request.POST.get("price")

        product.save()

        return redirect("/products/")
    
    return render(request, "edit_product.html", {
        "product": product 
    })


def create_product(request):

    if request.method == "POST":

        name = request.POST.get("name")
        price = request.POST.get("price")

        Product.objects.create(
            name=name,
            price=price
        )

    return render(request, "create_product.html")


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

    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })


def users(request):
    context = {
        "name": "NAME",
        "age": 18
    }
    return render(request, "user.html", context)
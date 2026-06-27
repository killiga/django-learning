from django.contrib import admin
from django.urls import path
from game.views import hello, about, contacts, news, products, users, create_subscription, subscriptions, edit_subscription


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("contacts/", contacts),
    path("news/", news),
    path("products/", products),
    path("users/", users),
    path("create-subscription/", create_subscription),
    path("edit-subscription/<int:id>/", edit_subscription),
    path("about/", about),
    path("subscriptions/", subscriptions),
]
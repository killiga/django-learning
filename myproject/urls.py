from django.contrib import admin
from django.urls import path
from game.views import hello, about, contacts, news, products, users, create_subscription, edit_product, delete_product, subscriptions


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("contacts/", contacts),
    path("news/", news),
    path("products/", products),
    path("users/", users),
    path("create-subscription/", create_subscription),
    path("edit-product/<int:id>/", edit_product),
    path("delete-product/<int:id>/", delete_product),
    path("about/", about),
    path("subscriptions/", subscriptions),
]
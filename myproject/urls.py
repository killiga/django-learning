from django.contrib import admin
from django.urls import path
from game.views import hello, about, contacts, news, products, users, create_product, edit_product, delete_product


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("contacts/", contacts),
    path("news/", news),
    path("products/", products),
    path("user/", users),
    path("create-product/", create_product),
    path("edit-product/<int:id>/", edit_product),
    path("delete-product/<int:id>/", delete_product),
    path("about/", about)
]
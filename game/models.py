from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(
    default="Описание пока не добавлено"
    )
    
    def __str__(self):
        return self.name
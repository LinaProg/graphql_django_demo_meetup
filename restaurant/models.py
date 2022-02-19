from django.db import models

# Create your models here.
class Ingridient(models.Model):
    name = models.CharField(max_length=255)
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()

class Dish(models.Model):
    name = models.CharField(max_length=255)
    grams = models.FloatField()
    cost = models.FloatField()
    in_menu = models.BooleanField(default=True)
    ingridients = models.ManyToManyField(Ingridient)


class Order(models.Model):
    address = models.TextField()
    paid = models.BooleanField(default=False, blank=True)
    ready = models.BooleanField(default=False, blank=True)
    delivered = models.BooleanField(default=False, blank=True)
    dishes = models.ManyToManyField(Dish)


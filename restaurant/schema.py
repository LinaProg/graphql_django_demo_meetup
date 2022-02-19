from dataclasses import field
import graphene
import graphene_django
from restaurant.forms import OrderForm
from restaurant.models import Ingridient, Order, Dish
from graphene_django.forms.mutation import DjangoModelFormMutation

class IngridientsQuery(graphene_django.DjangoObjectType):
    class Meta:
        model = Ingridient
        field = ("name", "proteins", "fats", "carbohydrates")


class DishQuery(graphene_django.DjangoObjectType):
    class Meta:
        model = Dish
        fields = ("name", "grams", "cost", "in_menu", "ingridients", "id")


class OrderQuery(graphene_django.DjangoObjectType):
    class Meta:
        model = Order
        fields = ("address", "paid", "ready", "delivered", "dishes")


class RestaurantQuery(graphene.ObjectType):
    ingridients = graphene.List(IngridientsQuery)
    dishes = graphene.List(DishQuery)
    orders = graphene.List(
        OrderQuery,
        paid = graphene.Boolean(required=False))


    def resolve_ingridients(self, info):
        return Ingridient.objects.all()

    def resolve_dishes(self, info):
        return Dish.objects.filter(in_menu = True)

    def resolve_orders(self, info, paid=None):
        orders = Order.objects.all()
        if paid: 
            orders = orders.filter(paid=True)
        elif paid is False: 
            orders = orders.filter(paid=False)
        return orders



class OrderMutation(DjangoModelFormMutation):
    class Meta:
        form_class = OrderForm
        data_type = OrderQuery


class RestaraurantMutation(graphene.ObjectType):
    make_order = OrderMutation.Field()
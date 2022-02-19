from django import forms
from restaurant.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= ("address", "paid", "dishes")

        
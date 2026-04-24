from django.shortcuts import render
from .models import FoodItems
# Create your views here.


def home(request):
    return render(request, "index.html")


def menu(request):
    items = FoodItems.objects.all()
    types = FoodItems.objects.values_list('Type', flat=True).distinct()
    return render(request, "menu.html", {
        "food_items": items,
        "food_types": types
    })


def book(request):
    return render(request, "book.html")


def about(request):
    return render(request, "about.html")

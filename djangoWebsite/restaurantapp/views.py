from django.shortcuts import render, HttpResponse
from .models import FoodItems
# Create your views here.


def home(request):
    return render(request, "index.html")


def menu(request):
    items = FoodItems.objects.all()
    return render(request, "menu.html", {"food_items": items})


def book(request):
    return render(request, "book.html")


def about(request):
    return render(request, "about.html")

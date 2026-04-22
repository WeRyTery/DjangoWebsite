from django.shortcuts import render, HttpResponse
from .models import FoodItems
# Create your views here.


def home(request):
    return render(request, "filter.html")


def menu(request):
    items = FoodItems.objects.all()
    return render(request, "menu.html", {"menu_items": items})

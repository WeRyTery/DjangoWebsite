from django.contrib import admin
from .models import FoodItems


class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Calories')
    search_fields = ('Name',)
    list_filter = ('Calories', 'Price')


# Register your models here.
admin.site.register(FoodItems, FoodItemsAdmin)

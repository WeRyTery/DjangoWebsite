from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class FoodItems(models.Model):
    FOOD_TYPES = [
        ('meat', 'Meat'),
        ('soup', 'Soup'),
        ('garnish', 'Garnish'),
        ('hot drinks', 'Hot drinks'),
        ('cold drinks', 'Cold drinks'),
        ('alcohol', 'Alcohol')
    ]

    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50, choices=FOOD_TYPES)
    Ingredients = ArrayField(models.CharField(max_length=100), blank=False)
    Calories = models.IntegerField()
    Price = models.FloatField(max_length=20)
    Image_path = models.CharField(max_length=200)

# TODO: Add images

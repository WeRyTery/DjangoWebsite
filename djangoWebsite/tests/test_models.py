from django.test import TestCase
from restaurantapp.models import FoodItems


class TestFoodItemsModel(TestCase):
    def test_model(self):
        items = FoodItems.objects.create(
            Name="Pizza test",
            Type="Pizza test",
            Ingredients=[("dought", "souce", "test")],
            Calories=1968,
            Price=500,
            Image_path="images/f6.png"
        )

        self.assertEqual(items.Name, "Pizza test")
        self.assertEqual(items.Price, 500)
        self.assertEqual(items.Type, "Pizza test")
        self.assertEqual(items.Calories, 1968)

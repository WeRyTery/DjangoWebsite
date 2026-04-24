from restaurantapp.models import FoodItems
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_home_page_laod(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_menu_page_laod(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_laod(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_booking_page_laod(self):
        response = self.client.get(reverse("book"))
        self.assertEqual(response.status_code, 200)

    def test_menu_contains_food(self):
        items = FoodItems.objects.create(
            Name="Test Burger",
            Type="Meat",
            Ingredients=[("Burger")],
            Price=500,
            Calories=1000
        )
        response = self.client.get(reverse('menu'))
        self.assertContains(response, "Test Burger")

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class ProductListViewTests(TestCase):
    def test_product_list_view_status_code(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_template(self):
        response = self.client.get("/products/")
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_should_return_200(self):
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.context['products']), 0)
        self.assertEqual(response.context["products"].count(), 0)

    def test_should_return_products(self):
        url = reverse("product_list")
        Product.objects.create(name="Espresso", price=2.5)
        Product.objects.create(name="Latte", price=3.5)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.context['products']), 2)
        self.assertEqual(response.context["products"].count(), 2)

    def test_api_product_list(self):
        url = reverse("product_list_api")
        Product.objects.create(name="Cappuccino", price=3.0)
        Product.objects.create(name="Mocha", price=4.0)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

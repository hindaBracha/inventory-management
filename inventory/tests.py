from django.test import TestCase

from .models import Product

class ProductTestCase(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Test Product", price=10.0)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.0)

import unittest
import sqlite3
from domain.product import Product
from mappers.product_mapper import ProductMapper

class TestProductMapper(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.mapper = ProductMapper(self.connection)

    def test_insert_and_find(self):
        product = Product(1, "Tablet", 299.99)
        self.mapper.insert(product)
        found = self.mapper.find(1)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Tablet")

    def test_list_all(self):
        self.mapper.insert(Product(1, "Tablet", 299.99))
        self.mapper.insert(Product(2, "Monitor", 199.99))
        products = self.mapper.list_all()
        self.assertEqual(len(products), 2)

if __name__ == "__main__":
    unittest.main()

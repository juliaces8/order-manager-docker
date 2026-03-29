import os
import unittest
from src.models import Order
from src.controller import OrderManager


class TestOrderManager(unittest.TestCase):

    def setUp(self):
        """Runs before every test. Uses a dedicated test file."""
        self.test_file = "test_orders.txt"
        self.manager = OrderManager(filename=self.test_file)

    def tearDown(self):
        """Runs after every test. Deletes the test file to keep clean."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_order_object_creation(self):
        """Use Case 1: Testing if an Order object is created correctly."""
        order = Order("101", "John Doe", "Guitar", 500.0)
        self.assertEqual(order.customer, "John Doe")
        self.assertEqual(order.instrument, "Guitar")

    def test_order_string_formatting(self):
        """Use Case 2: Testing if the __str__ method formats correctly."""
        order = Order("101", "John Doe", "Guitar", 500.0)
        expected_format = "101|John Doe|Guitar|500.0"
        self.assertEqual(str(order), expected_format)

    def test_invalid_price_validation(self):
        """Use Case 3: Testing Business Logic (Price must be positive)."""
        success, message = self.manager.add_order(
            "102", "Jane", "Flute", "-50"
        )
        self.assertFalse(success)
        self.assertIn("must be a positive number", message)

    def test_non_numeric_price(self):
        """Use Case 4: Testing Business Logic (Price must be a number)."""
        success, message = self.manager.add_order(
            "103", "Bob", "Drums", "abc"
        )
        self.assertFalse(success)
        self.assertIn("must be a number", message)

    def test_delete_order(self):
        """Use Case 5: Testing Delete Functionality."""
        self.manager.add_order("999", "Temp", "Flute", "100")
        success, message = self.manager.delete_order("999")
        self.assertTrue(success)
        self.assertIn("deleted successfully", message)

    def test_update_order_price(self):
        """Use Case 6: Testing Update Functionality."""
        self.manager.add_order("555", "EditMe", "Piano", "5000")
        success, message = self.manager.update_order("555", "5500.0")
        self.assertTrue(success)
        orders = self.manager.get_all_orders()
        self.assertIn("555|EditMe|Piano|5500.0", orders)


if __name__ == "__main__":
    unittest.main()

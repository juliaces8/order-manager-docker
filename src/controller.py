import os
from .models import Order
from .constants import FILENAME


class OrderManager:
    """Handles the logic of adding and retrieving orders."""

    def __init__(self, filename=FILENAME):
        self.filename = filename

    def add_order(self, order_id, customer, instrument, price):
        """Validates data and saves it to the file."""
        try:
            # Check if price is a valid positive number
            clean_price = float(price)
            if clean_price <= 0:
                return False, "Error: Price must be a positive number."

            # Create the Order object from our Model
            new_order = Order(order_id, customer, instrument, clean_price)

            # Save it to the text file (Append mode)
            with open(self.filename, "a") as file:
                file.write(str(new_order) + "\n")

            return True, "Order saved successfully!"

        except ValueError:
            return False, "Error: Price must be a number (e.g., 500.00)."

    def get_all_orders(self):
        """Reads the file and returns a list of all orders."""
        if not os.path.exists(self.filename):
            return []

        orders_list = []
        with open(self.filename, "r") as file:
            for line in file:
                line_content = line.strip()
                if line_content:  # Skip empty lines
                    orders_list.append(line_content)
        return orders_list

    def delete_order(self, order_id):
        """Removes an order by ID."""
        orders = self.get_all_orders()
        new_orders = [o for o in orders if not o.startswith(f"{order_id}|")]

        if len(orders) == len(new_orders):
            return False, f"Error: Order ID {order_id} not found."

        with open(self.filename, "w") as f:
            for o in new_orders:
                f.write(o + "\n")
        return True, f"Order {order_id} deleted successfully."

    def update_order(self, order_id, new_price):
        """Updates the price of an existing order."""
        try:
            val_price = float(new_price)
            orders = self.get_all_orders()
            updated = False
            new_data = []

            for line in orders:
                if line.startswith(f"{order_id}|"):
                    parts = line.split("|")
                    parts[-1] = str(val_price)
                    new_data.append("|".join(parts))
                    updated = True
                else:
                    new_data.append(line)

            if not updated:
                return False, f"Error: Order ID {order_id} not found."

            with open(self.filename, "w") as f:
                for line in new_data:
                    f.write(line + "\n")
            return True, "Order updated successfully."
        except ValueError:
            return False, "Error: New price must be a number."

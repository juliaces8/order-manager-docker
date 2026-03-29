class Order:
    """Represents a single musical instrument order."""

    def __init__(self, order_id, customer, instrument, price):
        self.order_id = order_id
        self.customer = customer
        self.instrument = instrument
        self.price = price

    def __str__(self):
        """Converts the order object into a string for the text file."""
        return f"{self.order_id}|{self.customer}|{self.instrument}|" \
               f"{self.price}"

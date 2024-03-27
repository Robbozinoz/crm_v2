# order.py

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.status = "Pending"

    def display_order(self):
        print(f"Customer: {self.customer.name}, Product: {self.product.name}, Quantity: {self.quantity}")

    def calculate_total_price(self):
        return self.quantity * self.product.price

    def cancel_order(self):
        self.status = "Cancelled"

    def track_shipment(self):
        # Placeholder logic: Track shipment using a tracking number
        return "Shipment is in transit"

    def get_order_details(self):
        # Placeholder logic: Retrieve detailed order information
        return {"Customer": self.customer.name, "Product": self.product.name, "Quantity": self.quantity}

    def update_status(self, new_status):
        self.status = new_status

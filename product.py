# product.py

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.inventory = 0
        self.sales_history = []
        self.cost_price = 0  # Placeholder value

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price}, Description: {self.description}")

    def update_price(self, new_price):
        self.price = new_price

    def check_availability(self, quantity):
        return self.inventory >= quantity

    def add_to_inventory(self, quantity):
        self.inventory += quantity

    def get_sales_history(self):
        return self.sales_history

    def calculate_profit_margin(self):
        # Placeholder logic: Calculate profit margin
        return (self.price - self.cost_price) / self.price  # Placeholder value

from customer import Customer
from product import Product
from order import Order
from project import Project
from invoice import Invoice

# Create a customer
customer1 = Customer("John Doe", "john@example.com", "1234567890")

# Create a product
product1 = Product("Laptop", 999, "A high-performance laptop")

# Create an order
order1 = Order(customer1, product1, 2)

# Create a project
project1 = Project("Website Development", "Developing a corporate website", customer1)

# Create an invoice
invoice1 = Invoice(order1, 1998)

# Display information
print("Customer Information:")
customer1.display_info()

print("\nProduct Information:")
product1.display_info()

print("\nOrder Information:")
order1.display_order()

print("\nProject Information:")
project1.display_info()

print("\nInvoice Information:")
invoice1.display_info()

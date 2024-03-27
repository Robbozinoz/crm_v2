# main.py
import datetime
# Import statements for all classes
from customer import Customer
from order import Order
from invoice import Invoice
from project import Project
from product import Product

if __name__ == "__main__":
    # Create a sample customer
    customer1 = Customer("John Doe", "john@example.com", "123-456-7890")

    # Update contact info
    customer1.update_contact_info(new_email="john.doe@example.com")

    # Add a note
    customer1.add_note("Called customer for follow-up")

    # Calculate lifetime value
    lifetime_value = customer1.calculate_lifetime_value()
    print("Customer Lifetime Value:", lifetime_value)

    # Retrieve recent orders
    recent_orders = customer1.get_recent_orders()
    print("Recent Orders:", recent_orders)

    # Send email notification
    customer1.send_email_notification("Special Offer", "Check out our latest deals!")

    # Create a sample product
    product1 = Product("Laptop", 1000, "High-performance laptop")

    # Update price
    product1.update_price(1200)

    # Check availability
    is_available = product1.check_availability(5)
    print("Product Availability:", is_available)

    # Add to inventory
    product1.add_to_inventory(10)

    # Get sales history
    sales_history = product1.get_sales_history()
    print("Sales History:", sales_history)

    # Calculate profit margin
    profit_margin = product1.calculate_profit_margin()
    print("Profit Margin:", profit_margin)

    # Create a sample order
    order1 = Order(customer1, product1, 2)

    # Display order details
    order1.display_order()

    # Calculate total price
    total_price = order1.calculate_total_price()
    print("Total Price:", total_price)

    # Cancel order
    order1.cancel_order()

    # Track shipment
    shipment_status = order1.track_shipment()
    print("Shipment Status:", shipment_status)

    # Get order details
    order_details = order1.get_order_details()
    print("Order Details:", order_details)

    # Update order status
    order1.update_status("Shipped")

    # Create a sample invoice
    invoice1 = Invoice(order1, total_price)

    # Display invoice info
    invoice1.display_info()

    # Generate invoice PDF
    invoice1.generate_invoice_pdf()

    # Send invoice email
    invoice1.send_invoice_email()

    # Record payment
    invoice1.record_payment(800)

    # Calculate outstanding balance
    outstanding_balance = invoice1.calculate_outstanding_balance()
    print("Outstanding Balance:", outstanding_balance)

    # Schedule payment reminder
    invoice1.schedule_payment_reminder()

    # Create a sample project
    project1 = Project("Website Redesign", "Redesigning company website", customer1)

    # Display project info
    project1.display_info()

    # Add a task
    project1.add_task("Design homepage")

    # Update progress
    project1.update_progress(50)

    # Assign team member
    project1.assign_team_member("Designer")

    # Generate project report
    project1.generate_project_report()

    # Set deadline
    project1.set_deadline(datetime.datetime(2024, 5, 1))

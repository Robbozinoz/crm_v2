# customer.py
import datetime
import csv

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.notes = []

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}")

    def update_contact_info(self, new_email=None, new_phone=None):
        if new_email:
            self.email = new_email
        if new_phone:
            self.phone = new_phone

    def add_note(self, note):
        self.notes.append(note)

    def calculate_lifetime_value(self):
        # Placeholder logic: Calculate lifetime value based on historical purchases
        return 1000  # Placeholder value

    def get_recent_orders(self, num_orders=5):
        # Placeholder logic: Retrieve recent orders for the customer
        return ["Order1", "Order2", "Order3", "Order4", "Order5"]

    def send_email_notification(self, subject, message):
        # Placeholder logic: Print email notification message
        print(f"Email sent to {self.email}: Subject - {subject}, Message - {message}")

    
    # Reporting
    def save_to_csv(self):
        with open(self.CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.email, self.phone])

    @classmethod
    def load_from_csv(cls):
        customers = []
        with open(cls.CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                customers.append(cls(*row))
        return customers
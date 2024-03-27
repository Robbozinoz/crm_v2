import csv

class Customer:
    # Define CSV file format
    CSV_FILE = "customers.csv"

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

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

    # Other methods...

# Similar implementations for other classes (Product, Order, Invoice, Project)

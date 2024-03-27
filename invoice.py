# invoice.py

class Invoice:
    def __init__(self, order, amount, status="Pending"):
        self.order = order
        self.amount = amount
        self.status = status
        self.recorded_payments = 0

    def display_info(self):
        print(f"Order: {self.order.display_order()}, Amount: ${self.amount}, Status: {self.status}")

    def generate_invoice_pdf(self):
        # Placeholder logic: Generate PDF invoice document
        print("Invoice PDF generated")

    def send_invoice_email(self):
        # Placeholder logic: Send invoice via email
        print("Invoice sent via email")

    def record_payment(self, payment_amount):
        # Placeholder logic: Record payment and update status
        self.recorded_payments += payment_amount
        print(f"Payment of ${payment_amount} recorded")

    def calculate_outstanding_balance(self):
        return self.amount - self.recorded_payments  # Placeholder value

    def schedule_payment_reminder(self):
        # Placeholder logic: Schedule payment reminder
        print("Payment reminder scheduled")

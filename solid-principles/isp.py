# Interface Segregation Principle

# Interface for payment processing
class PaymentProcessor:
    def process_payment(self, amount):
        pass


# Interface for payment refunding
class RefundProcessor:
    def refund_payment(self, amount):
        pass


# Class for processing payments only
class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Implementation to process payment goes here
        print("Payment processed successfully:", amount)


# Class for processing and refunding payments
class OnlineRefundPaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        # Implementation to process payment goes here
        print("Payment processed successfully:", amount)

    def refund_payment(self, amount):
        # Implementation to refund payment goes here
        print("Payment refunded successfully:", amount)


# Example usage
payment_processor = OnlinePaymentProcessor()
refund_payment_processor = OnlineRefundPaymentProcessor()

payment_processor.process_payment(1000)     
refund_payment_processor.process_payment(500)

refund_payment_processor.refund_payment(200)

from abc import ABC, abstractmethod

# Interface for processing payments
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Interface for processing refunds
class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

# Class that implements the PaymentProcessor interface
class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

# Class that implements both PaymentProcessor and RefundProcessor interfaces
class FullPaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")


def client(payment_processor):
    if isinstance(payment_processor, PaymentProcessor):
        payment_processor.process_payment(100)
    if isinstance(payment_processor, RefundProcessor):
        payment_processor.process_refund(50)


online_payment_processor = OnlinePaymentProcessor()
full_payment_processor = FullPaymentProcessor()

client(online_payment_processor)  
client(full_payment_processor)    

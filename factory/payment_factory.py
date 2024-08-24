""""
Credit Card: Requires a card number, cardholder name, and expiry date. The system should check if the card is valid before processing.
PayPal: Requires an email address and a password for authentication.
Cryptocurrency (e.g., Bitcoin): Requires a wallet address and an amount in BTC.
Additionally, the system should:

Log each payment in a payment history database (just a list for simplicity).
Provide a mechanism to extend the payment system with new methods without modifying the existing code (e.g., support for future payment types like Apple Pay, Google Pay, etc.).
Your task is to:

Create an abstract class PaymentMethod that defines a process_payment method.
Implement concrete classes for CreditCardPayment, PayPalPayment, and CryptoPayment.
Create a PaymentFactory that returns the correct payment object based on user input.
Log each processed payment in a payment history list.
Ensure the factory can be easily extended to support additional payment methods.
""""


from abs import ABC 
from enum import Enum

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass
    
class TextLogger(Logger):
    def __init__(self, file_location):
        self.file  = open(file_location, 'a')
    def log(self, message): 
        self.file.write(f"{message} \n")

class LokiLogger(Logger):
    def __init__(self, url):
        self.url = url
    
    def log(self, message):
        #loki push message 
        pass

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount_to_pay):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_holder_name, cvv, bank): 
        self.card_holder_name = card_holder_name
        self.cvv = cvv 
        self.bank = bank
        self.logger = TextLogger("/log/file.txt")
    
    def validate_method(self):
        pass
    
    def process_payment(self, amount_to_pay)
        self.logger.log("Processing payment")
        #update db 
        self.logger.log("Completed payment")

class PayPalPayment(PaymentMethod):
    def __init__(self,id, user_name, bank): 
        self.id= id
        self.user_name=user_name
        self.bank = bank
        self.logger = TextLogger("/log/file.txt")
    
    def validate_method(self):
        pass
    
    def process_payment(self, amount_to_pay)
        self.logger.log("Processing payment")
        #update db 
        self.logger.log("Completed payment")
        

class CryptoPayment(PaymentMethod):
    def __init__(self, crypto_wallet, crypto_name, bank): 
        self.wallet_id = crypto_wallet
        self.crypto_name = crypto_name
        self.bank = bank 
        self.logger = TextLogger("/log/file.txt")
    
    def validate_method(self):
        pass
    
    def process_payment(self, amount_to_pay)
        self.logger.log("Processing payment")
        #update db 
        self.logger.log("Completed payment")

# class PaymentFactory():
#     @staticmethod
#     def payment_method(payment_type, **kwargs): 
#         if payment_type == "card": 
#             return CreditCardPayment(kwargs["card_holder_name"], kwargs["cvv"], kwargs["bank"])
#         elif payment_type == "paypal": 
#             return PayPalPayment(kwargs["id"], kwargs["user_name"], kwargs["bank"])
#         elif payment_type == "crypto": 
#             return CreditCardPayment(kwargs["crypto_wallet"], kwargs["crypto_name"], kwargs["bank"])
#         else: 
#             print("Error")
        
# card_payment = PaymentFactory.payment_method("card", card_holder_name="John", cvv="344", bank="JPMorgan")
# card_payment.process_payment(100)


class PaymentFactory(ABC): 
    @abstractmethod
    def create(**kwargs): 
        pass
class CreditCardPaymentFactory(ABC): 
    @staticmethod
    def create(**kwargs): 
        return CreditCardPayment(kwargs["card_holder_name"], 
        kwargs["cvv"], kwargs["bank"])

class PayPalPaymentFactory(ABC): 
    @staticmethod
    def create(**kwargs): 
        return PayPalPayment(kwargs["card_holder_name"], 
        kwargs["cvv"], kwargs["bank"])
        
class CryptoPaymentFactory(ABC): 
    @staticmethod
    def create(**kwargs): 
        pass
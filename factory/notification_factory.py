"""
Question:

You are building a system that handles various types of notifications (e.g., email, SMS, and push notifications). Each notification type has its own unique method for sending messages.

Email notifications require a recipient email address and a subject line.
SMS notifications require a phone number and a message body.
Push notifications require a device ID and a notification title.
Design a notification system using the factory design pattern. Implement a factory that returns the correct notification object based on the notification type.
"""

from abs import ABC 
from enum import Enum

class Notification(ABC):
    @abstractmethod 
    def send(self):
        pass

class EmailNotification(Notification):
    def __init__(self, email, subject):
        self.email = email
        self.subject = subject 
    
    def send(self):
        print(f"Sending Email to {self.email} \
        with subject {self.subject}")

def SMSNotification(Notification):
    def __init__(self, number, message):
        self.number = number 
        self.message = message 
    
    def send(self): 
        print(f"Sending SMS {self.number}\
        with the message {self.message}")

def PushNotification(Notification):
    def __init__(self,device_id, message):
        self.device_id = device_id
        self.message = message
    
    def send(self): 
        print(f"Pushing notificaition {self.device_id}\
        with the message {self.message}")

class NotificationFactory(ABC):
    @abstractmethod
    def get_notification(self):
        pass

class EmailNotificationFactory(NotificationFactory):
    @staticmethod
    def get_notification(notification_type, **kwargs):
        if notification_type == "email":
            return EmailNotification(kwargs["email"]. kwargs["subject"])
        elif notification_type == "sms":
            return SMSNotification(kwargs["number"]. kwargs["message"])
        elif notification_type == "push":
            return PushNotification(kwargs["device_id"]. kwargs["message"])
        else: 
            raise ValueError(f"Unknown notification type")


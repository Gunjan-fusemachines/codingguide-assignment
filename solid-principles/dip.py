# dependency inversion principle

# Abstraction for email sending functionality
from abc import ABC, abstractmethod

class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass


# Concrete implementation of the email sending functionality
class ConcreteEmailSender(EmailSender):
    def send_email(self, recipient, subject, message):
        # Implementation to send an email goes here
        print(f"Email sent to: {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")


# Notification service with dependency on EmailSender abstraction
class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_notification(self, recipient, subject, message):
        self.email_sender.send_email(recipient, subject, message)


# Example usage
email_sender = ConcreteEmailSender()
notification_service = NotificationService(email_sender)

notification_service.send_notification("abcxyz@fusemachines.com", "assignment day 3", "dependency inversion principle")

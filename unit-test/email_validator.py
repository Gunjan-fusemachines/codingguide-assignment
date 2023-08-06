import re

def validate_email(email):
    # Regular expression to check email format
    email_format = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Valid email providers
    valid_providers = ['yahoo', 'gmail', 'outlook']

    # Check if email matches the format
    if not re.match(email_format, email):
        return False

    # Extract domain from the email
    domain = email.split('@')[1]

    # Check if domain is a valid provider
    if domain.split('.')[0] not in valid_providers:
        return False

    # Check for disposable email providers
    disposable_providers = ['yopmail']
    if domain.split('.')[0] in disposable_providers:
        return False

    return True

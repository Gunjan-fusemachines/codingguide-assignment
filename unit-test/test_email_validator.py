import unittest
from email_validator import validate_email

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email('user@yahoo.com'))
        self.assertTrue(validate_email('user@gmail.com'))
        self.assertTrue(validate_email('user@outlook.com'))

    def test_invalid_emails(self):
        self.assertFalse(validate_email('user@example.com'))
        self.assertFalse(validate_email('user@yopmail.com'))
        self.assertFalse(validate_email('user@gmail'))
        self.assertFalse(validate_email('user@gmail.'))
        self.assertFalse(validate_email('user@outlook'))

if __name__ == '__main__':
    unittest.main()

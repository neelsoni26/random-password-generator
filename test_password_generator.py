import string
import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_no_special_chars(self):
        password = generate_password(12, chars=string.ascii_letters + string.digits)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in password))

    def test_only_digits(self):
        password = generate_password(8, chars=string.digits)
        self.assertTrue(all(c in string.digits for c in password))

if __name__ == '__main__':
    unittest.main()

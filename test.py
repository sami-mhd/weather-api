import unittest
from server import app  # Make sure this import points to your server module

class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()  # Use the Flask test client
        cls.app.testing = True  # Enable testing mode

    def test_index_route(self):
        response = self.app.get('/')  # Call the index route
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertIn(b'<!DOCTYPE html>', response.data)  # Check for HTML document

if __name__ == '__main__':
    unittest.main()
import unittest
from server import app  # Make sure this import points to your server module

class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()  # Use the Flask test client
        cls.app.testing = True  # Enable testing mode

    def test_index_route(self):
        response = self.app.get('/')  # Call the index route
        self.assertEqual(response.status_code, 200)  # Check if response is OK
        self.assertIn(b'<!DOCTYPE html>', response.data)  # Check for HTML document

if __name__ == '__main__':
    unittest.main()

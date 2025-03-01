import unittest
from lectai import LectAI

class TestLectAI(unittest.TestCase):
    def setUp(self):
        self.client = LectAI(base_url="https://hidden-endpoint-url.com")

    def test_get_response(self):
        response = self.client.get_response("Hello, Lect AI!")
        self.assertIsInstance(response, dict)

if __name__ == "__main__":
    unittest.main()
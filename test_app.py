import unittest
import json
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_index_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_number(self):
        response = self.app.post('/', data=dict(number=5))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Number submitted successfully!')

    def test_data_written_to_file(self):
        self.app.post('/', data=dict(number=5))
        with open('data.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data['number'], '5')

if __name__ == '__main__':
    unittest.main()
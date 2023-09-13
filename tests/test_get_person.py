import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api'

class TestGetPerson(unittest.TestCase):

    def test_get_nonexistent_person(self):
        response = requests.get(f'{BASE_URL}/999')  # Assuming there's no person with ID 999
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Person not found')

    def test_get_person_with_invalid_id(self):
        response = requests.get(f'{BASE_URL}/invalid_id')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Invalid user_id')

    def test_get_person_success(self):
        response = requests.get(f'{BASE_URL}/1')  # Assuming there's a person with ID 1
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())

if __name__ == '__main__':
    unittest.main()


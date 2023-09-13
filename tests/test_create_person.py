import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api'

class TestCreatePerson(unittest.TestCase):

    def test_create_person_with_missing_data(self):
        data = {}  # Missing 'name' field
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Name is required')

    def test_create_person_with_empty_name(self):
        data = {'name': ''}
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Name is required')

    def test_create_person_with_special_characters(self):
        data = {'name': '@#$%'}
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Invalid characters in name')

    def test_create_person_with_long_name(self):
        data = {'name': 'A' * 1000}  # A very long name
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Name is too long')

    def test_create_person_success(self):
        data = {'name': 'John Doe'}
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'John Doe created successfully')

if __name__ == '__main__':
    unittest.main()


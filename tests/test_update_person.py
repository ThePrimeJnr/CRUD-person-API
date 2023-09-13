import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api'

class TestUpdatePerson(unittest.TestCase):

    def test_update_person_with_empty_name(self):
        data = {'name': ''}
        response = requests.put(f'{BASE_URL}/1', json=data)  # Assuming there's a person with ID 1
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Name is required')

    def test_update_nonexistent_person(self):
        data = {'name': 'Updated Name'}
        response = requests.put(f'{BASE_URL}/999', json=data)  # Assuming there's no person with ID 999
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Person not found')

    def test_update_person_success(self):
        data = {'name': 'Updated Name'}
        response = requests.put(f'{BASE_URL}/1', json=data)  # Assuming there's a person with ID 1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Updated Name updated successfully')

if __name__ == '__main__':
    unittest.main()


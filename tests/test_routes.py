import unittest
import requests

# Replace with the URL of your running API
BASE_URL = 'http://127.0.0.1:5000/api'

class TestPersonAPI(unittest.TestCase):

    def test_create_person(self):
        data = {'name': 'John Doe'}
        response = requests.post(f'{BASE_URL}', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'John Doe created successfully')

    def test_get_person(self):
        response = requests.get(f'{BASE_URL}/1')  # Assuming there's a person with ID 1
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())

    def test_update_person(self):
        data = {'name': 'Updated Name'}
        response = requests.put(f'{BASE_URL}/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Updated Name updated successfully')

    def test_delete_person(self):
        data = {'name': 'Delete Me'}
        response = requests.post(f'{BASE_URL}', json=data)  # Create a person for deletion
        self.assertEqual(response.status_code, 201)

        response = requests.delete(f'{BASE_URL}/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Delete Me deleted successfully')

if __name__ == '__main__':
    unittest.main()


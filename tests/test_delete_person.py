import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api'

class TestDeletePerson(unittest.TestCase):

    def test_delete_nonexistent_person(self):
        response = requests.delete(f'{BASE_URL}/999')  # Assuming there's no person with ID 999
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Person not found')

    def test_delete_person(self):
        data = {'name': 'Delete Me'}
        response = requests.post(f'{BASE_URL}', json=data)  # Create a person for deletion
        self.assertEqual(response.status_code, 201)

        response = requests.delete(f'{BASE_URL}/{response.json()[user_id]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Delete Me deleted successfully')

if __name__ == '__main__':
    unittest.main()


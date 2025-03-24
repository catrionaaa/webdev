import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_games(self):
        response = self.client.get('/api/games')
        self.assertEqual(response.status_code, 200)

    def test_create_game_unauthorized(self):
        response = self.client.post('/api/games', json={"mode": "Snap"})
        self.assertEqual(response.status_code, 403)  # Expecting admin key error

if __name__ == '__main__':
    unittest.main()
import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_games(self):
        response = self.client.get('/api/games', headers={'X-API-KEY': 'ad18364d5b3f50b20234c13821fe26e5e111a5128c6d3f8d19ed70cdaa4c8add'})
        self.assertEqual(response.status_code, 200)

    def test_create_game_unauthorized(self):
        response = self.client.post('/api/games', json={"mode": "snap"})
        self.assertEqual(response.status_code, 403)  # Expecting admin key error

    def test_update_game(self):
        response = self.client.put('/api/games', json={"id": 0, "mode": "TEST"}, headers={'X-API-KEY': 'ad18364d5b3f50b20234c13821fe26e5e111a5128c6d3f8d19ed70cdaa4c8add'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
import requests

class DeckOfCardsAPI:
    BASE_URL = "https://deckofcardsapi.com/api/deck"

    @staticmethod
    def new_deck(deck_count=1):
        response = requests.get(f"{DeckOfCardsAPI.BASE_URL}/new/shuffle/?deck_count={deck_count}")
        return response.json()

    @staticmethod
    def draw_cards(deck_id, count=1):
        response = requests.get(f"{DeckOfCardsAPI.BASE_URL}/{deck_id}/draw/?count={count}")
        return response.json()

    @staticmethod
    def shuffle_deck(deck_id):
        response = requests.get(f"{DeckOfCardsAPI.BASE_URL}/{deck_id}/shuffle/")
        return response.json()
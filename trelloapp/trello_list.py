import requests
from .trello_card import TrelloCard


class TrelloList:

    def __init__(self, list_id, name, api_key, api_token):
        self.list_id = list_id
        self.name = name
        self.api_key = api_key
        self.api_token = api_token
        self.cards = {}

    def add_card(self, card_name, card_description):
        url = "https://api.trello.com/1/cards"
        query = {
            'key': self.api_key,
            'token': self.api_token,
            'idList': self.list_id,
            'name': card_name,
            'desc': card_description
        }

        try:
            response = requests.post(url, params=query)
            response.raise_for_status()
            if response.status_code == 200:
                card_data = response.json()
                new_card = TrelloCard(card_data['id'], card_data['name'], card_data['desc'], self.api_key,
                                      self.api_token)
                self.cards[new_card.card_id] = new_card
                print("Card added successfully!")
                return card_data
            else:
                print(f"Failed to add card. Status code: {response.status_code}")
                print(f"Response: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while adding the card to Trello: {e}")
            return None

    def fetch_cards(self):
        url_cards = f"https://api.trello.com/1/lists/{self.list_id}/cards"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        try:
            response = requests.get(url_cards, params=query)
            response.raise_for_status()
            cards = response.json()
            for card in cards:
                self.cards[card['id']] = TrelloCard(card['id'], card['name'], card['desc'], self.api_key,
                                                    self.api_token)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching cards for list {self.list_id}: {e}")

import requests
from .trello_list import TrelloList

class TrelloBoard:
    def __init__(self, board_id, api_key, api_token):
        self.board_id = board_id
        self.api_key = api_key
        self.api_token = api_token
        self.lists = {}

    def fetch_lists_and_cards(self):
        url_lists = f"https://api.trello.com/1/boards/{self.board_id}/lists"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        try:
            response_lists = requests.get(url_lists, params=query)
            response_lists.raise_for_status()
            lists = response_lists.json()
            for trello_list in lists:
                new_list = TrelloList(trello_list['id'], trello_list['name'], self.api_key, self.api_token)
                new_list.fetch_cards()
                self.lists[new_list.list_id] = new_list
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data from Trello: {e}")

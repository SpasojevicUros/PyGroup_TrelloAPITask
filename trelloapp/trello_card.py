import requests

class TrelloCard:
    def __init__(self, card_id, name, description, api_key, api_token):
        self.card_id = card_id
        self.name = name
        self.description = description
        self.api_key = api_key
        self.api_token = api_token

    def update(self, new_name=None, new_description=None):
        url = f"https://api.trello.com/1/cards/{self.card_id}"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        if new_name is not None:
            query['name'] = new_name

        if new_description is not None:
            query['desc'] = new_description

        try:
            response = requests.put(url, params=query)
            response.raise_for_status()
            if response.status_code == 200:
                self.name = new_name if new_name else self.name
                self.description = new_description if new_description else self.description
                print("Card updated successfully!")
                return response.json()
            else:
                print(f"Failed to update card. Status code: {response.status_code}")
                print(f"Response: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating the card on Trello: {e}")
            return None

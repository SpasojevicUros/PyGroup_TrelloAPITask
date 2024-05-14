import requests
import json
import time

from config import API_KEY, API_TOKEN, TABLE_ID

def get_lists(my_table):
    try:
        url = f"https://api.trello.com/1/boards/{TABLE_ID}/lists"
        
        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': API_KEY,
            'token': API_TOKEN
        }

        response = requests.get(
            url,
            headers=headers,
            params=query
        )

        if response.status_code == 200:
            for list in response.json():
                my_table[list['id']]  = {"name": list["name"], "cards": {}}
        else:
            print(f"An error occurred: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def get_cards(my_table):
    try:
        url = f"https://api.trello.com/1/boards/{TABLE_ID}/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': API_KEY,
            'token': API_TOKEN
        }

        response = requests.get(
            url,
            headers=headers,
            params=query
        )

        if response.status_code == 200:
            for card in response.json():
                my_table[card['idList']]['cards'][card['id']] = {"name": card["name"], "desc": card["desc"]}
        else:
            print(f"An error occurred: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def add_card(list_id, name, desc):
    try:
        url = "https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'idList': list_id,
            'key': API_KEY,
            'token': API_TOKEN,
            'name': name,
            'desc': desc
        }

        response = requests.post(
            url,
            headers=headers,
            params=query
        )

        if response.status_code == 200:
            print("Card added successfully")
            time.sleep(2)
        else:
            print(f"An error occurred: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    my_table = {}
    get_lists(my_table)  
    get_cards(my_table)
    print(json.dumps(my_table, indent=4))
    
    list_id = list(my_table.keys())[0]
    name = "New Card"
    desc = "This is a new card"
    
    print(f"listid: {list_id}, name: {name}, desc: {desc}")
    
    add_card(list_id, name, desc)
    
    get_cards(my_table)
    print(json.dumps(my_table, indent=4))

if __name__ == "__main__":
    main()
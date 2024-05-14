import requests
import json
import time
import os

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
        
        response = requests.get(url, headers=headers, params=query)
        
        if response.status_code == 200:
            for list in response.json():
                my_table[list['id']] = {"name": list['name'], "cards": {}}
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None

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

        response = requests.get(url, headers=headers, params=query)

        if response.status_code == 200:
            for card in response.json():
                my_table[card['idList']]['cards'][card['id']] = {"name": card['name'], "desc": card['desc']}
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None

def add_new_card(list_id, card_name, card_desc):
    try:
        url = f"https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': API_KEY,
            'token': API_TOKEN,
            'idList': list_id,
            'name': card_name,
            'desc': card_desc
        }
        
        response = requests.post(url, headers=headers, params=query)
        
        if response.status_code == 200:
            print_colored("Card added successfully.", 1)
            time.sleep(2)
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None
    
def print_table(my_table):
    for list_id, list in my_table.items():
        print(f"\nList: {list['name']}")
        for card_id, card in list['cards'].items():
            print(f"    Card: {card['name']}")
            print_colored(f"        Desc: {card['desc']}", 2)

def print_colored(text: str, color_code: int, end='\n'):
    """
    Print the text in the specified color.
    
    Args:
    - text (str): The text to print.
    - color_code (int): The color code (1 for green, 2 for yellow, 3 for red, 4 for blue, 5 for cyan).
    """
    # ANSI escape codes for the colors
    colors = {
        1: '\033[92m', # Green
        2: '\033[93m', # Yellow
        3: '\033[91m', # Red
        4: '\033[94m', # Blue
        5: '\033[96m', # Cyan
    }
    # Reset code to reset the color to default after printing
    reset = '\033[0m'
    
    # Get the color escape code from the dictionary, default to no color if not found
    color_escape_code = colors.get(color_code, '')
    
    # Print the colored text followed by the reset code to return to default color
    print(f"{color_escape_code}{text}{reset}", end=end)

def clean_screen():
    os.system('cls')

def display_options():
    print_colored("\nOptions:", 4)
    print_colored("1. Add new card", 4)
    print_colored("2. Exit", 4)

def handle_user_input(my_table):
    print_colored("Enter the option number: ", 5, end='')
    option = input()
    if option == '1':
        print_colored("What list would you like to add the card to?", 4)
        for list_id, list_item in my_table.items():
            print(f"{list_id}: {list_item['name']}")
        print_colored("Enter the list id: ", 4, end='')
        list_id = input()
        if list_id not in my_table:
            print_colored("Invalid list id. Please try again.", 3)
        else:
            print_colored("Enter the card name: ", 4, end='')
            card_name = input()
            print_colored("Enter the card description: ", 4, end='')
            card_desc = input()
            if card_name and card_desc:
                add_new_card(list_id, card_name, card_desc)
    elif option == '2':
        return False
    else:
        print_colored("Invalid option selected. Please try again.", 3)
    return True

def get_input(my_table):
    while True:
        clean_screen()
        get_lists(my_table)
        get_cards(my_table)
        print_colored("Current table format:", 4)
        print_table(my_table)
        display_options()
        if not handle_user_input(my_table):
            break

def main():
    my_table = {}
    get_input(my_table)

if __name__ == "__main__":
    main()
            
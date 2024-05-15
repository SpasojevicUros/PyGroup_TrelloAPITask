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
            for t_list in response.json():
                my_table[t_list['id']] = {"name": t_list['name'], "cards": {}}
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
    
def remove_card(card_id):
    try:
        url = f"https://api.trello.com/1/cards/{card_id}"

        query = {
            'key': API_KEY,
            'token': API_TOKEN
        }

        response = requests.delete(
            url,
            params=query
        )

        if response.status_code == 200:
            print_colored("Card removed successfully.", 1)
            time.sleep(2)
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None
    
def update_card(card_id, card_name, card_desc):
    try:
        url = f"https://api.trello.com/1/cards/{card_id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': API_KEY,
            'token': API_TOKEN,
            'name': card_name,
            'desc': card_desc
        }

        response = requests.put(url, headers=headers, params=query)

        if response.status_code == 200:
            print_colored("Card updated successfully.", 1)
            time.sleep(2)
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None
    
def print_table(my_table):
    for list_id, t_list in my_table.items():
        print(f"\nList: {t_list['name']}")
        for card_id, card in t_list['cards'].items():
            print(f"    Card: {card['name']}")
            print_colored(f"        Desc: {card['desc']}", 2)
            
def make_folder():
    if not os.path.exists('./OUTPUT'):
        os.makedirs('./OUTPUT')
            
def export_to_csv(my_table):
    try:
        make_folder()
        with open('./OUTPUT/table.csv', 'w', encoding="utf-8") as f:
            f.write('List Name,Card Name,Card Description\n')
            for list_id, t_list in my_table.items():
                for card_id, card in t_list['cards'].items():
                    if card['desc'] is '':
                        desc = 'No description'
                    else:
                        desc = card['desc']
                    f.write(f"{t_list['name']},{card['name']},{desc}\n")
        print_colored("Table exported to table.csv", 1)
        time.sleep(2)
    except Exception as e:
        print(e)
        input("Press Enter to continue...")

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
    print_colored("2. Update a card", 4)
    print_colored("3. Remove a card", 4)
    print_colored("4. Exit", 4)
    print_colored("\n\n9. Export to CSV", 4)

def handle_user_input(my_table):
    print_colored("Enter the option number: ", 5, end='')
    option = input()
    if option == '1':
        print_colored("What list would you like to add the card to?", 4)
        list_ids = list(my_table.keys())
        for i, list_id in enumerate(list_ids, 1):
            print(f"{i}: {my_table[list_id]['name']}")
        print_colored("Enter the list number: ", 4, end='')
        list_index = int(input()) - 1
        if list_index not in range(len(list_ids)):
            print_colored("Invalid list number. Please try again.", 3)
        else:
            list_id = list_ids[list_index]
            print_colored("Enter the card name: ", 4, end='')
            card_name = input()
            print_colored("Enter the card description: ", 4, end='')
            card_desc = input()
            if card_name and card_desc:
                add_new_card(list_id, card_name, card_desc)
    elif option == '2':
        print_colored("What card do you want to update?", 4)
        card_map = {}
        idx = 1
        for list_id, t_list in my_table.items():
            for card_id, card in t_list['cards'].items():
                card_map[idx] = card_id
                print(f"{idx}: {card['name']}")
                idx += 1
        print_colored("Enter the card number: ", 4, end='')
        card_index = int(input())
        card_id = card_map.get(card_index)
        if card_id:
            print_colored("Enter the new card name: ", 4, end='')
            card_name = input()
            print_colored("Enter the new card description: ", 4, end='')
            card_desc = input()
            if card_name and card_desc:
                update_card(card_id, card_name, card_desc)
    elif option == '3':
        print_colored("What card do you want to remove?", 4)
        card_map = {}
        idx = 1
        for list_id, t_list in my_table.items():
            for card_id, card in t_list['cards'].items():
                card_map[idx] = card_id
                print(f"{idx}: {card['name']}")
                idx += 1
        print_colored("Enter the card number: ", 4, end='')
        card_index = int(input())
        card_id = card_map.get(card_index)
        if card_id:
            remove_card(card_id)
    elif option == '4':
        return False
    elif option == '9':
        export_to_csv(my_table)
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
            
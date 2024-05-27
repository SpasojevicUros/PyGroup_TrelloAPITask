import os
import json
import requests
import logging

logger = logging.getLogger(__name__)

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_to_file(data, filename):
    if not os.path.exists("./BACKUP"):
        os.makedirs("./BACKUP")
    with open(f'./BACKUP/{filename}', "w") as file:
        json.dump(data, file, indent=4)
        
def load_from_file(filename):
    with open(filename, "r") as file:
        return json.load(file)
    
def download_file(data):

    url = data['url']
    file_path = f"./BACKUP/{data['name']}-{data['id']}.jpeg"

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        logger.info(f"File downloaded to {file_path}")
    else:
        logger.error(f"Failed to download file: {response.status_code}")
    
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
    
def display_menu():
    print("Trello Management System")
    print("========================")
    print("1. Download board data")
    print("2. Display board content")
    print("3. Display Attachments")
    print("4. Upload board data")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def clean_screen():
    os.system('cls')
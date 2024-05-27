import os
import time
import logging
import coloredlogs

from dotenv import load_dotenv
from trello_client import TrelloClient
from file_display import FileDisplay
from utils import save_to_file, download_file, clean_screen, display_menu

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_TOKEN = os.getenv("API_TOKEN")
BOARD_ID = os. getenv("BOARD_ID")

# Config
LOG = True
COLORED_LOGS = False

# Set up logging
if LOG:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    if COLORED_LOGS:
        coloredlogs.install(level='DEBUG', logger=logger)
                    
if __name__ == "__main__":
    
    client = TrelloClient(API_KEY, API_TOKEN, BOARD_ID)
    display = FileDisplay("./BACKUP/")
    
    while True:
        clean_screen()
        choice = display_menu()
        
        match choice:
            case '1':
                clean_screen()
                board, attachments = client.load_board_data()
                for attachment in attachments:
                    download_file(attachment)
                save_to_file(board.to_dict(), "board.json")
                print("Board data downloaded and saved to board.json.")
            
            case '2':
                clean_screen()
                display.display_board_content()
            
            case '3':
                clean_screen()
                display.display_files_by_format('jpeg')
            
            case '4':
                clean_screen()
                client.upload_board_data()
                print("Board data uploaded successfully.")
            
            case '5':
                clean_screen()
                print("Exiting...")
                time.sleep(1.5)
                break
            
            case _:
                print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")
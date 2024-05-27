import json
import os
from models.board import Board

class FileDisplay:
    def __init__(self, directory):
        self.directory = directory

    def list_files(self):
        files = os.listdir(self.directory)
        for file in files:
            print(file)
            
    def display_files_by_format(self, file_format: str):
        try:
            files = os.listdir(self.directory)
            
            filtered_files = [file for file in files if file.endswith(file_format)]
            
            if filtered_files:
                print(f"Attachments:")
                for file in filtered_files:
                    print(f"    {file}")
            else:
                print(f"Attachments:")
                print(f"    No attachments on the board.")

        except FileNotFoundError:
            print(f"The folder '{self.directory}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_file_content(self, filename):
        filepath = os.path.join(self.directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                content = json.load(f)
                print(json.dumps(content, indent=4))
        else:
            print(f"{filename} does not exist in the directory.")

    def display_board_content(self):
        filepath = os.path.join(self.directory, 'board.json')
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                board_data = json.load(f)
                board = Board.from_dict(board_data)
                self._print_board(board)
        else:
            print("board.json does not exist in the directory.")

    def _print_board(self, board):
        print(f"Board ID: {board.id}")
        print(f"Name: {board.name}")
        print(f"Description: {board.desc}")
        print(f"URL: {board.url}")
        print("Lists:")
        for lst in board.lists:
            print(f"  List ID: {lst.id}")
            print(f"  Name: {lst.name}")
            print(f"  Cards:")
            for card in lst.cards:
                print(f"    Card ID: {card.id}")
                print(f"    Name: {card.name}")
                print(f"    Description: {card.desc}")
                if card.comments:
                    print(f"    Comments:")
                    for comment in card.comments:
                        print(f"      {comment.data['text']}")
import sys
from .trello_board import TrelloBoard

class TrelloApp:
    def __init__(self, api_key, api_token, board_id):
        self.api_key = api_key
        self.api_token = api_token
        self.board = TrelloBoard(board_id, api_key, api_token)

    def run(self):
        self.board.fetch_lists_and_cards()
        while True:
            print("\nOptions:")
            print("1. View all cards")
            print("2. Add a card")
            print("3. Update a card")
            print("4. Exit")

            choice = input("Enter the number of your choice: ")

            match choice:
                case '1':
                    self.view_all_cards()
                case '2':
                    self.add_card()
                case '3':
                    self.update_card()
                case '4':
                    print("Exiting program.")
                    sys.exit(0)
                case _:
                    print("Invalid choice. Please try again.")

    def view_all_cards(self):
        print("All cards in the board:")
        for trello_list in self.board.lists.values():
            print(f"List: {trello_list.name}")
            for card in trello_list.cards.values():
                print(f"  [] {card.name} (ID: {card.card_id})")
                print(f"        Description: {card.description}")

    def add_card(self):
        print("Available lists:")
        lists = list(self.board.lists.values())
        for i, trello_list in enumerate(lists):
            print(f"{i + 1}. {trello_list.name}")

        list_number = int(input("Enter the number of the list to add the card to: ")) - 1
        if list_number < 0 or list_number >= len(lists):
            print("Invalid list number.")
            return

        list_id_to_add = lists[list_number].list_id
        card_name = input("Enter the name of the card: ")
        card_desc = input("Enter the description of the card: ")

        self.board.lists[list_id_to_add].add_card(card_name, card_desc)

    def update_card(self):
        card_list = []
        print("Available cards:")
        for trello_list in self.board.lists.values():
            for card in trello_list.cards.values():
                card_list.append(card)
                print(f"{len(card_list)}. {card.name}")

        card_number_to_update = int(input("Enter the number of the card to update: ")) - 1
        if card_number_to_update < 0 or card_number_to_update >= len(card_list):
            print("Invalid card number.")
            return

        card_to_update = card_list[card_number_to_update]
        new_name = input("Enter the new name for the card (leave blank to keep the current name): ").strip()
        new_description = input("Enter the new description for the card (leave blank to keep the current description): ").strip()

        new_name = new_name if new_name else None
        new_description = new_description if new_description else None

        card_to_update.update(new_name, new_description)

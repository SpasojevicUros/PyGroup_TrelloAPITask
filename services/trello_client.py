from models.board import Board
from models.list import ListData
from models.card import Card
from models.checklist import CheckList
from models.comment import Comment

from request_client import RequestClient
from utils import load_from_file

import logging
logger = logging.getLogger(__name__)

class TrelloClient:
    
    def __init__(self, api_key, api_token, board_id):
        self.client = RequestClient("https://api.trello.com/1/", api_key, api_token)
        self.board_id = board_id
        logger.info("TrelloClient initialized with board ID: %s", board_id)
        
    def get_board(self):
        logger.info("Fetching board data")
        return self.client.get(f"boards/{self.board_id}")
    
    def get_lists(self):
        logger.info("Fetching lists data")
        return self.client.get(f"boards/{self.board_id}/lists")
    
    def get_cards(self):
        logger.info("Fetching cards data")
        return self.client.get(f"boards/{self.board_id}/cards")
    
    def get_checklists(self, card_id):
        logger.info("Fetching checklists data")
        return self.client.get(f"cards/{card_id}/checklists")
    
    def get_comments(self, card_id):
        logger.info("Fetching comments data")
        return self.client.get(f"cards/{card_id}/actions", {"filter": "commentCard"})
    
    def get_attachments(self, card_id):
        logger.info("Fetching attachments data")
        return self.client.get(f"cards/{card_id}/attachments")
    
    def _update_content(self):
        pass
    
    def add_new_list(self, board_id, list_name):
        logger.info("Adding new list")
        data = {
            "name": list_name,
            "idBoard": board_id
        }
        return self.client.post("lists", data=data)
    
    def add_new_card(self, list_id, card_name, card_desc):
        logger.info("Adding new card")
        data = {
            "idList": list_id,
            "name": card_name,
            "desc": card_desc
        }
        return self.client.post("cards", data=data)
    
    def remove_card(self, card_id):
        logger.info("Removing card")
        return self.client.delete(f"cards/{card_id}")
    
    def update_card(self, card_id, new_name, new_desc):
        logger.info("Updating card")
        data = {
            "name": new_name,
            "desc": new_desc
        }
        return self.client.put(f"cards/{card_id}", data=data)
    
    def add_checklist(self, card_id, checklist):
        pass
    
    def add_comment(self, card_id, comment):
        pass
    
    def load_board_data(self):
        logger.info("Loading board data")
        board_json = self.get_board()
        lists_json = self.get_lists()
        cards_json = self.get_cards()
        
        board = Board.from_dict(board_json)
        all_lists = [ListData.from_dict(data) for data in lists_json]
        cards = [Card.from_dict(data) for data in cards_json]
        
        attachments = []
        for card in cards:
            checklists_json = self.get_checklists(card.id)
            card.checkLists = [CheckList.from_dict(_data) for _data in checklists_json]
            
            comments_json = self.get_comments(card.id)
            card.comments = [Comment.from_dict(_data) for _data in comments_json]
            
            att_info = self.get_attachments(card.id)
            attachments.extend(att_info)
        
        for one_list in all_lists:
            one_list.cards = [card for card in cards if card.idList == one_list.id]
        
        board.lists = all_lists
        logger.info("Board data loaded successfully")
        return board, attachments
    
    def upload_board_data(self, path = './BACKUP/'):
        logger.info("Uploading board data")
        board_json = load_from_file(path + "board.json")
        board = Board.from_dict(board_json)
        
        for lst in board.lists[::-1]:
            self.add_new_list(self.board_id, lst.name)

        lists = self.get_lists()
        
        for lst in board.lists:
            for _lst in lists:
                if lst.name == _lst["name"]:
                    print(f"List {lst.name} == {_lst['name']}")
                    for card in lst.cards:
                        self.add_new_card(_lst["id"], card.name, card.desc)
        
        
        
        
        
    

    
        
    
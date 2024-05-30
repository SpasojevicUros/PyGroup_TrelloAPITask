from fastapi import FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from database import SessionLocal, Board, List, Card, Comment

app = FastAPI()

# Create a new list
@app.post("/list")
async def create_list(request: Request):
    data = await request.json()
    db = SessionLocal()
    try:
        db_list = List(name=data["name"], board_id=data["board_id"])
        db.add(db_list)
        db.commit()
        db.refresh(db_list)
        return db_list
    finally:
        db.close()

# Create a new card
@app.post("/card")
async def create_card(request: Request):
    data = await request.json()
    db = SessionLocal()
    try:
        db_card = Card(name=data["name"], list_id=data["list_id"])
        db.add(db_card)
        db.commit()
        db.refresh(db_card)
        return db_card
    finally:
        db.close()

# Retrieve a specific board and its lists and cards
@app.get("/boards/{board_id}")
def read_board(board_id: int):
    db = SessionLocal()
    try:
        board = db.query(Board).filter(Board.id == board_id).first()
        if board is None:
            raise HTTPException(status_code=404, detail="Board not found")
        lists = db.query(List).filter(List.board_id == board_id).all()
        for lst in lists:
            cards = db.query(Card).filter(Card.list_id == lst.id).all()
            lst.cards = cards
        board.lists = lists
        return board
    finally:
        db.close()

# Retrieve a specific card and its comments
@app.get("/cards/{card_id}")
def read_card(card_id: int):
    db = SessionLocal()
    try:
        card = db.query(Card).filter(Card.id == card_id).first()
        if card is None:
            raise HTTPException(status_code=404, detail="Card not found")
        comments = db.query(Comment).filter(Comment.card_id == card_id).all()
        card.comments = comments
        return card
    finally:
        db.close()

# Retrieve a specific list and its cards
@app.get("/lists/{list_id}")
def read_list(list_id: int):
    db = SessionLocal()
    try:
        list_ = db.query(List).filter(List.id == list_id).first()
        if list_ is None:
            raise HTTPException(status_code=404, detail="List not found")
        cards = db.query(Card).filter(Card.list_id == list_id).all()
        list_.cards = cards
        return list_
    finally:
        db.close()


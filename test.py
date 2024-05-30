from sqlalchemy.orm import Session
from database import SessionLocal, Board, List, Card

def populate_db():
    db = SessionLocal()
    try:
        # Create a new board
        board = Board(name="Project Board")
        db.add(board)
        db.commit()
        db.refresh(board)

        # Create lists
        todo_list = List(name="To Do", board_id=board.id)
        doing_list = List(name="Doing", board_id=board.id)
        done_list = List(name="Done", board_id=board.id)
        db.add(todo_list)
        db.add(doing_list)
        db.add(done_list)
        db.commit()
        db.refresh(todo_list)
        db.refresh(doing_list)
        db.refresh(done_list)

        # Create cards
        task1 = Card(name="Task 1", list_id=todo_list.id)
        task2 = Card(name="Task 2", list_id=doing_list.id)
        task3 = Card(name="Task 3", list_id=done_list.id)
        db.add(task1)
        db.add(task2)
        db.add(task3)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    populate_db()

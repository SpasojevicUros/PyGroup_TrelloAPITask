from sqlalchemy import create_engine, URL, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lists = relationship('List', back_populates='board')

class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    board_id = Column(Integer, ForeignKey('boards.id'))
    board = relationship('Board', back_populates='lists')
    cards = relationship('Card', back_populates='list')

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship('List', back_populates='cards')
    checklists = relationship('Checklist', back_populates='card')
    comments = relationship('Comment', back_populates='card')

class Checklist(Base):
    __tablename__ = 'checklists'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    card_id = Column(Integer, ForeignKey('cards.id'))
    card = relationship('Card', back_populates='checklists')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    card_id = Column(Integer, ForeignKey('cards.id'))
    card = relationship('Card', back_populates='comments')
    
url = URL.create(
    "sqlite",
    database="test.db"
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
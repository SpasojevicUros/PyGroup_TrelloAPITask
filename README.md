# FastAPI and SQLAlchemy Project

This project demonstrates a simple CRUD application using FastAPI and SQLAlchemy with an SQLite database. The application allows you to create and retrieve boards, lists, cards, checklists, and comments.

## Project Structure

- `database.py`: Contains database models and setup.
- `main.py`: Contains FastAPI application and API endpoints.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn

## Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Install the dependencies:

    ```bash
    pip install fastapi sqlalchemy uvicorn
    ```

## Running the Application

1. Ensure that the `database.py` and `main.py` files are in the project directory.

2. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

## Endpoints

- `POST /list`: Create a new list.
- `POST /card`: Create a new card.
- `GET /boards/{board_id}`: Retrieve a specific board and its lists and cards.
- `GET /cards/{card_id}`: Retrieve a specific card and its comments.
- `GET /lists/{list_id}`: Retrieve a specific list and its cards.

## Database Initialization

The database will be created automatically if it does not exist when you run the application for the first time.

## TODO

1. **Baza podataka i modeli**
   - [x] Kreirati SQLAlchemy modele za Trello elemente (Board, List, Card, Checklist, Comment).
   - [ ] (Optional)Istražiti korišćenje postojećih data klasa iz prethodnog zadatka.
   - [x] Deklarisati relacije između tabela u SQLAlchemy modelima.

2. **Klasa za konekciju na bazu podataka**
   - [ ] Kreirati klasu za upravljanje konekcijom na bazu podataka, uključujući engine i session.
   - [ ] Implementirati CRUD operacije u okviru ove klase za jednostavniju interakciju sa bazom podataka.

3. **FastAPI aplikacija**
   - [x] Kreirati FastAPI aplikaciju.
   - [x] Definisati endpoint-e:
     - [x] `GET /boards/{board_id}`
     - [x] `GET /cards/{card_id}`
     - [x] `GET /lists/{list_id}`
     - [x] `POST /card`
     - [x] `POST /list`
   - [ ] (Optional) Dodati endpoint-e za ažuriranje i brisanje elemenata.
   - [ ] Koristiti Trello API za kreiranje elemenata na Trello prilikom kreiranja lista ili kartica.
   - [ ] Sačuvati elemente u bazi podataka nakon uspešnog kreiranja na Trello.

5. **Održavanje koda**
   - [x] Dodati završeni kod na Git repository.

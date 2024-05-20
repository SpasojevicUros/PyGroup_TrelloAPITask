# Trello Board Manager

This script provides a command-line interface for managing a Trello board. It allows you to fetch lists and cards, add new cards, update and remove existing cards, and export the board data to a CSV file.

## Features

- **Fetch Lists and Cards**: Retrieve lists and cards from your Trello board and store them in a local dictionary.
- **Add New Card**: Add a new card to a specified list.
- **Update Card**: Update the name and description of an existing card.
- **Remove Card**: Remove an existing card (or cards) from the board.
- **Export to CSV**: Export the board data to a CSV file.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/trello-board-manager.git
    cd trello-board-manager
    ```

2. Install the required library:

    ```bash
    pip install requests
    ```

3. Create a `config.py` file in the same directory and add your Trello API credentials:

    ```python
    API_KEY = 'your_api_key'
    API_TOKEN = 'your_api_token'
    TABLE_ID = 'your_table_id'
    ```

## Usage

Run the script:

```bash
python main.py

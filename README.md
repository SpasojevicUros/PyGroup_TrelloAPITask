# Trello Management System

This script provides a command-line interface for managing a Trello board. It allows you to download board data, display board content, display files by format, upload board data, and print the directory tree of your work folder.

## Features

- **Download Board Data**: Retrieve lists, cards, checklists, comments, and attachments from your Trello board and save them to a local JSON file.
- **Display Board Content**: Display the content of the board in a readable format.
- **Display Files by Format**: Display files in the specified format from the backup directory.
- **Upload Board Data**: Upload the local board data back to Trello, ensuring no duplicates.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- `coloredlogs` library (optional)

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/SpasojevicUros/PyGroup_TrelloAPITask.git
    cd PyGroup_TrelloAPITask
    ```

2. Install the required libraries:

    ```bash
    pip install requests python-dotenv coloredlogs
    ```

3. Create a `.env` file in the same directory and add your Trello API credentials:

    ```dotenv
    API_KEY=your_api_key
    API_TOKEN=your_api_token
    BOARD_ID=your_board_id
    ```

## Usage

Run the script:

```bash
python main.py
```

### Menu Options
1. Download board data: Downloads the board data from Trello and saves it to board.json.
2. Display board content: Displays the content of the board stored in board.json.
3. Display files by format: Prompts for a file format and displays files matching that format from the backup directory.
4. Upload board data: Uploads the local board data from board.json to Trello.
6. Exit: Exits the application.

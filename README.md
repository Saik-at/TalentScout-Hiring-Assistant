#  IPL MCP Server — Natural Language Cricket Analytics

This project implements an **MCP (Model Context Protocol) Server** that answers natural language questions about IPL matches using structured match data. It supports integration with **Claude Desktop** and provides both CLI and web-based testing.

---

##  Features

- Parse JSON IPL match data from [cricsheet.org](https://cricsheet.org/)
- Store structured data in **SQLite** (SQL only, no NoSQL)
- Query match, player, and performance info using natural language
- MCP server built with **Flask**
- Supports integration with **Claude Desktop**
- Includes CLI tester and web-based interface

---

##  Folder Structure

assignment/
├── data/ # JSON IPL match files (min 5)
├── db/ # SQLite DB with match + delivery tables
├── queries/ # Natural language to SQL mapping
│ └── query_map.py
├── scripts/
│ └── parse_and_load.py # Script to parse JSON and populate DB
├── server/
│ └── app.py # Flask MCP server
├── test_client.py # CLI tool for testing questions
├── requirements.txt # Python dependencies
└── README.md # This file


---

## ⚙️ Installation

### 1. Clone the Repository

In terminal:
git clone https://github.com/your-username/ipl-mcp-server.git
cd ipl-mcp-server

### 2. Install Requirements

pip install -r requirements.txt

### 3. Add IPL Match Files
Download at least 5 JSON match files from:

https://cricsheet.org/matches/

Place them in the data/ folder.

### 4. Load the Data
Run the parser script to populate the SQLite database:

python scripts/parse_and_load.py

This creates db/ipl_matches.sqlite and loads match + delivery data.

### 5. Run the MCP Server

python server/app.py

Server will run at:

http://127.0.0.1:5000

### 6. Test Questions (Natural Language)

Type in terminal:
python test_client.py

You will get a menu of supported questions. Choose a number to test.


### 7. Sample Questions Supported
Show me all matches in the dataset

Which team won the most matches?

What was the highest total score?

Show matches played in Mumbai

Who scored the most runs across all matches?

Which bowler took the most wickets?

Show me Virat Kohli's batting stats

What’s the average first innings score?

Which venue has the highest scoring matches?

Show me all centuries scored

More queries can easily be added via query_map.py

### 8. Claude Desktop Integration
Claude should connect to this server via:

Endpoint: http://localhost:5000/ask

Method: POST

Content-Type: application/json

Payload Format:

{
  "question": "Which team won the most matches?"
}

The server will respond with structured results:

{
  "results": [
    { "winner": "MI", "wins": 5 }
  ]
}


### 9. Submission Instructions
 Include ≥5 IPL JSON files in data/

 Ensure SQLite DB is built using parse_and_load.py

 Confirm app.py runs and answers sample questions

 Include test_client.py and test_web.html

 Document Claude integration in this README

### 10. Thanks & Credits
Match data from Cricsheet, licensed under Creative Commons Attribution 3.0.

Built with 💡, 🐍 Python, and 🏏 IPL love.
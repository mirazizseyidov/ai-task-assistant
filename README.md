# AI-Powered Task Assistant (CLI v1.0)

This is a Python-based command-line tool designed to help manage software development tasks. It uses an AI agent (built with the Google GenAI SDK) that can automatically understand user requests and use local Python functions (tools) to calculate project metrics and save reports to text files.

---

## Project Development Journal

### Step 1 – 24.04 (Initial Idea)
Goal
Create a simple AI-assisted tool that helps developers estimate task deadlines and automatically generate basic report files without performing manual calculations.
AI Approach
The system uses a lightweight prompt-based AI approach where the user enters a natural language request, and the AI extracts important information such as task name, estimated hours, and difficulty level.
Planned Tools
Calculator Function — used for estimating working hours and calculating approximate deadlines.
File Writer Function — used for automatically generating and saving report files in formats such as .txt or .md.
Concepts Needed
The project is based on several core Python programming concepts:
Functions
Basic string parsing
File handling
Simple automation logic
Natural language input processing
Expected Result
The final system should allow users to quickly enter task descriptions, automatically calculate estimated completion times, and generate structured reports with minimal manual work

### Step 2 – 08.05 (Implementation Progress)
* **What I actually did:** I upgraded the project to use the official `google-genai` SDK and the `gemini-2.5-flash` model. Instead of parsing text manually, I used the model's native Tool Calling feature (`automatic_function_calling`).
* **Concepts Used:** I used Object-Oriented Programming (OOP) to build the agent class, type hints, and Python docstrings. The docstrings are very important because Gemini reads them to understand what the tools do and how to use them.

### Step 3 – 15.05 (Testing and Data Handling)
* **Testing Process:** I wrote automated unit tests using Python’s built-in `unittest` framework to check the tools locally without making real API calls every time.
* **Scenarios Tested:** I verified that the calculator handles different task difficulties correctly, checked how it responds to invalid input strings, and ensured files are created and cleaned up properly.
* **Data Conversion:** When a user types a request like *"10 hours, hard task"*, the AI converts that unstructured text into clean data types (integers and strings), sends them to the Python functions, and formats the output back into an easy-to-read response.

### Final Submission – 22.05 (Final Synthesis)
* **Final System:** The system is now fully complete and working as an interactive CLI application.
* **Conclusions:** The tests pass successfully, proving that the local tools work reliably. The AI does a great job acting as the coordinator between the user input and the backend functions.
* **Deployment Strategy:** Right now, the application runs locally in the terminal as a CLI tool. If I were to deploy this into production in the future, I would wrap the Python code in a web API using FastAPI and package it inside a Docker container so it could easily connect to a front-end website or a Discord/Telegram bot.

---

## Project Structure

```text
ai-task-assistant/
│
├── agent.py            # Sets up the Gemini AI model and registers the tools
├── tools.py            # The actual Python functions (calculator, file saver)
├── main.py             # The main terminal loop for user interaction
├── requirements.txt    # External libraries needed (google-genai, python-dotenv)
├── .env.example        # A template showing where to put your Gemini API key
└── tests/
    └── test_system.py  # Unit tests to verify the tools work correctly

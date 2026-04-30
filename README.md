# AI Finance Assistant

An intelligent agent that processes natural language financial inputs and uses tools to convert them into a unified currency.

## How to Run
1. **Clone the repo:** `git clone https://github.com/mirazizseyidov/ai-task-assistant.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the program:** `python src/main.py`
4. **Run tests:** `python tests/test_system.py`

---

## Project Journal

### Step 1 – 24.04 (Initial Concept)
- **System Goal:** Automate currency conversion for personal expense tracking using an AI agent.
- **Tools:** `get_exchange_rate` and `calculate_expense`.
- **Approach:** Modular Python system where an agent identifies currency patterns in text.

### Step 2 – 08.05 (Implementation)
- **Status:** Core logic completed.
- **Concepts Applied:** 
    - **OOP:** Created a `FinanceAgent` class to handle requests.
    - **Modularization:** Separated tools, agent logic, and main execution.
    - **Regex:** Used regular expressions for data extraction from user strings.

### Step 3 – 15.05 (Testing & Deployment)
- **Testing:** Implemented functional testing in `tests/test_system.py` to verify tool accuracy.
- **Data Conversion:** System converts string inputs (e.g., "USD") into numerical floats and performs cross-currency calculations.
- **Deployment Strategy:** This system is designed as a Command-Line Interface (CLI) tool.

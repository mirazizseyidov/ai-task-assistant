# AI Finance Assistant

An intelligent agent that processes natural language financial inputs and uses tools to convert them into a unified currency.

## How to Run
1. **Clone the repo:** `git clone https://github.com/mirazizseyidov/ai-task-assistant.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the program:** `python src/main.py`
4. **Run tests:** `python tests/test_system.py`

---

## Project Journal

### Step 1 – 24.04 (Initial Design)
- **Goal:** Develop an AI-based agent that automates currency conversion for expense tracking.
- **Tools:** `get_exchange_rate` and `calculate_expense`.
- **Approach:** Modular Python system using regex for entity extraction.

### Step 2 – 08.05 (Implementation)
- **Status:** Core logic and folder structure completed.
- **Concepts Applied:** 
    - **OOP:** Encapsulated logic within the `FinanceAgent` class.
    - **Modularity:** Separated code into `tools.py`, `agent.py`, and `main.py`.
    - **Regex:** Used for pattern matching to extract numerical data and currency codes.

### Step 3 – 15.05 (Testing & Data Conversion)
- **Testing Process:** Performed functional testing of the main workflow and tools using `tests/test_system.py`.
- **Test Scenarios:**
    1. **Scenario:** User inputs "I spent 100 USD". 
       - **Expected:** "100 USD. In RUB: 9250.0". 
       - **Result:** PASSED.
    2. **Scenario:** User inputs "Lunch 20 EUR". 
       - **Expected:** "20 EUR. In RUB: 2000.0". 
       - **Result:** PASSED.
    3. **Scenario:** Invalid text input. 
       - **Expected:** Error handling message. 
       - **Result:** PASSED.

## Data Porting and Conversion
The system ensures data consistency by transforming unstructured input into structured types:
1. **Input:** Raw user string (e.g., "50 USD").
2. **Extraction:** The Agent uses `re.search` to extract the amount and currency code.
3. **Conversion:** The amount string is cast to `float`, and the currency string is normalized to uppercase.
4. **Consistency:** These typed variables are passed to the tools to ensure mathematical accuracy.

## System Deployment Strategy
The chosen deployment strategy for this software is a **Local Command-Line Tool**.
- **Reasoning:** This allows for safe, local testing of the agent's logic without external server dependencies.
- **Setup:** Users can run the system by installing dependencies from `requirements.txt` and executing the `main.py` script.
- **Future Scale:** The modular architecture allows for easy migration to a Web Service (API) or a Chatbot interface.

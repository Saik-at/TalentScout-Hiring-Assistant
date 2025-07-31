# TalentScout Hiring Assistant

An interactive Streamlit-based AI Hiring Assistant that collects candidate information and generates tailored technical interview questions based on the candidate's declared tech stack.

## Features

- Simple and intuitive UI built with **Streamlit**
- Collects essential candidate details:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position(s)
  - Current Location
  - Tech Stack
- Generates **3–5 technology-specific questions** per skill
- Simulated conversation with:
  - **Follow-up interaction support**
  - **Conversation history tracking**
- Allows candidate to **exit the interview** using keywords like `exit`, `quit`, or `bye`
- Clean and modular code with separation of logic (`app.py`, `prompts.py`, `llm_replicate.py`)

## Note on LLM Usage

Due to lack of working API keys or credits for services like OpenAI, HuggingFace, and Replicate, this project does **not use a live LLM**.

Instead, the backend uses:
- Static or rule-based prompt-response logic
- Pre-engineered responses per tech stack keyword
- Simulated follow-up using templated logic

This fallback approach still demonstrates key capabilities of prompt handling, session state, and conversational structure, without depending on paid model APIs.

## File Structure


├── app.py # Main Streamlit application
├── prompts.py # Prompt construction logic
├── question_engine.py # Simulated LLM response logic (no API required)
├── README.md # Documentation


---
## Install dependencies:
pip install -r requirements.txt

## Run the Streamlit app:
streamlit run app.py

 ### Assignment Goals Fulfilled
 Candidate info collection

 Tech-based question generation

 Exit keyword detection

 Follow-up handling and context memory

 Graceful session close

 README and modular file structure

## Sample Run

### Input:
- Name: Saikat Jana  
- Email: jana@example.com  
- Position: Data Analyst  
- Tech Stack: Python, SQL

### Output:
Questions for Python:

What are Python's key data types?

Explain the difference between a list and a tuple.

What are decorators and how are they used?
...

Questions for SQL:

Explain different types of JOINs in SQL.

What is the difference between WHERE and HAVING?
...


---

## Future Improvements

- Switch to real LLM APIs once access is available (e.g., OpenAI, Replicate, Hugging Face)

---

## Author

Submitted as part of an AI/ML Internship Assignment.

This project demonstrates LLM application structure, prompt engineering, and fallback planning even when live inference is not available.


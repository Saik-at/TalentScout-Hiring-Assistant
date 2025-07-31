# TalentScout Hiring Assistant 

A Streamlit-based chatbot that simulates an AI-powered Hiring Assistant. It collects candidate information and generates technical interview questions based on their tech stack — designed to showcase LLM usage principles even without live API access.

---

## Features

- Collects candidate details (name, email, phone, experience, etc.)
- Generates skill-specific technical questions
- Clean and interactive Streamlit UI
- Uses static question logic to simulate LLM behavior
- Reset and reuse the assistant for multiple candidates

---

## Tech Stack

- **Python 3.10+**
- **Streamlit** for frontend
- **Prompt Simulation Logic** in Python
- *Originally designed for integration with Hugging Face, OpenAI, or Replicate models*

---

## Note on LLM Integration

The original assignment objective was to use an LLM (like Mistral or LLaMA) to generate contextual interview questions.

> However, due to **limited access to gated APIs** (e.g., Hugging Face, Replicate) and **lack of active API credits**, I was unable to connect to a real hosted LLM model.

### Workaround Implemented

To still demonstrate prompt design and project flow:
- I implemented a **static prompt-response simulation**
- The questions resemble what a real LLM would generate
- All logic is modular, so APIs can be easily plugged in when available

---

## How to Run

1. Make sure dependencies are installed:
    ```bash
    pip install streamlit
    ```

2. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## File Structure


├── app.py # Main Streamlit application
├── prompts.py # Prompt construction logic
├── llm_replicate.py # Simulated LLM response logic (no API required)
├── README.md # Documentation


---

## Sample Run

### Input:
- Name: Jane Doe  
- Email: jane@example.com  
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
- Add PDF or CSV export of interview questions
- Add multilingual or sentiment-aware features

---

## Author

Submitted as part of an AI/ML Internship Assignment.

This project demonstrates LLM application structure, prompt engineering, and fallback planning even when live inference is not available.


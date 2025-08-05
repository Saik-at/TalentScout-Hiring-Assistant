import requests

# List of supported test questions
questions = [
    "Show me all matches in the dataset",
    "Which team won the most matches?",
    "What was the highest total score?",
    "Show matches played in Mumbai",
    "Who scored the most runs across all matches?",
    "Which bowler took the most wickets?",
    "Show me Virat Kohli's batting stats",
    "What’s the average first innings score?",
    "Which venue has the highest scoring matches?",
    "Show me all centuries scored"
]

def show_menu():
    print("\n📋 Choose a question to ask the MCP Server:\n")
    for idx, question in enumerate(questions, start=1):
        print(f"{idx}. {question}")
    print("0. Exit\n")

def ask_question(q):
    url = "http://127.0.0.1:5000/ask"
    try:
        res = requests.post(url, json={"question": q})
        res.raise_for_status()
        result = res.json()

        if "results" in result:
            if result["results"]:
                print("\n📊 Server Response:\n")
                for i, row in enumerate(result["results"], 1):
                    print(f"{i}. {row}")
            else:
                print("\n⚠️ No results found.")
        else:
            print("\n❌ Error:", result.get("error", "Unknown error."))

    except Exception as e:
        print("\n❌ Request failed:", str(e))

if __name__ == "__main__":
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("👋 Exiting.")
                break
            elif 1 <= choice <= len(questions):
                ask_question(questions[choice - 1])
            else:
                print("❌ Invalid choice. Try again.")
        except ValueError:
            print("❌ Please enter a number.")

import os
import sys
import sqlite3
from flask import Flask, request, jsonify

# ✅ Forcefully add absolute path to import queries
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
QUERIES_DIR = os.path.join(BASE_DIR, 'queries')
if QUERIES_DIR not in sys.path:
    sys.path.insert(0, QUERIES_DIR)

# ✅ Direct import now works
from query_map import get_sql_for_question

app = Flask(__name__)
DB_PATH = os.path.join(BASE_DIR, "db", "ipl_matches.sqlite")

def run_query(sql, params=None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql, params or {})
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    sql, params = get_sql_for_question(question)
    if not sql:
        return jsonify({"error": "Sorry, I don't understand that question."}), 400

    try:
        results = run_query(sql, params)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

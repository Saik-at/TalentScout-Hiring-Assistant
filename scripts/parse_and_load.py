import os
import json
import sqlite3

DB_PATH = os.path.join("db", "ipl_matches.sqlite")
SCHEMA_PATH = os.path.join("db", "schema.sql")
DATA_DIR = "data"

def create_db():
    with open(SCHEMA_PATH, 'r') as f:
        schema = f.read()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def parse_and_insert_match(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    match_id = os.path.basename(json_file).replace(".json", "")
    info = data["info"]
    outcome = info.get("outcome", {})

    match_record = {
        "match_id": match_id,
        "city": info.get("city"),
        "venue": info.get("venue"),
        "date": info["dates"][0],
        "team1": info["teams"][0],
        "team2": info["teams"][1],
        "toss_winner": info["toss"]["winner"],
        "toss_decision": info["toss"]["decision"],
        "winner": outcome.get("winner"),
        "result": list(outcome.keys())[0] if outcome else None,
        "win_by_runs": outcome.get("by", {}).get("runs"),
        "win_by_wickets": outcome.get("by", {}).get("wickets"),
        "player_of_match": info.get("player_of_match", [None])[0]
    }

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO matches (match_id, city, venue, date, team1, team2, toss_winner, toss_decision,
                             winner, result, win_by_runs, win_by_wickets, player_of_match)
        VALUES (:match_id, :city, :venue, :date, :team1, :team2, :toss_winner, :toss_decision,
                :winner, :result, :win_by_runs, :win_by_wickets, :player_of_match)
    """, match_record)

    match_db_id = cur.lastrowid

    # Insert deliveries
    for inning_index, inning in enumerate(data.get("innings", []), start=1):
        batting_team = inning["team"]
        overs = inning["overs"]
        for over_data in overs:
            over = over_data["over"]
            for ball_index, delivery in enumerate(over_data["deliveries"]):
                d = {
                    "match_id": match_id,
                    "inning": inning_index,
                    "over": over,
                    "ball": ball_index + 1,
                    "batting_team": batting_team,
                    "bowling_team": info["teams"][1] if batting_team == info["teams"][0] else info["teams"][0],
                    "striker": delivery.get("batter"),
                    "non_striker": delivery.get("non_striker"),
                    "bowler": delivery.get("bowler"),
                    "runs_batter": delivery["runs"]["batter"],
                    "runs_extras": delivery["runs"]["extras"],
                    "runs_total": delivery["runs"]["total"],
                    "wicket_kind": delivery.get("wickets", [{}])[0].get("kind") if "wickets" in delivery else None,
                    "player_out": delivery.get("wickets", [{}])[0].get("player_out") if "wickets" in delivery else None
                }

                cur.execute("""
                    INSERT INTO deliveries (
                        match_id, inning, over, ball, batting_team, bowling_team,
                        striker, non_striker, bowler, runs_batter, runs_extras,
                        runs_total, wicket_kind, player_out
                    ) VALUES (
                        :match_id, :inning, :over, :ball, :batting_team, :bowling_team,
                        :striker, :non_striker, :bowler, :runs_batter, :runs_extras,
                        :runs_total, :wicket_kind, :player_out
                    )
                """, d)

    conn.commit()
    conn.close()

def load_all_matches():
    create_db()
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            print(f"Processing {file}...")
            parse_and_insert_match(os.path.join(DATA_DIR, file))
    print("Done.")

if __name__ == "__main__":
    load_all_matches()

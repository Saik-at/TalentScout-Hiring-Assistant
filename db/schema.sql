-- Matches table
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    city TEXT,
    venue TEXT,
    date TEXT,
    team1 TEXT,
    team2 TEXT,
    toss_winner TEXT,
    toss_decision TEXT,
    winner TEXT,
    result TEXT,
    win_by_runs INTEGER,
    win_by_wickets INTEGER,
    player_of_match TEXT
);

-- Deliveries table
CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    inning INTEGER,
    over INTEGER,
    ball INTEGER,
    batting_team TEXT,
    bowling_team TEXT,
    striker TEXT,
    non_striker TEXT,
    bowler TEXT,
    runs_batter INTEGER,
    runs_extras INTEGER,
    runs_total INTEGER,
    wicket_kind TEXT,
    player_out TEXT
);

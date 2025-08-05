def get_sql_for_question(question):
    q = question.lower()

    if "all matches" in q:
        return ("SELECT match_id, city, date, team1, team2, winner FROM matches", None)

    if "team won the most matches" in q:
        return ("""
            SELECT winner, COUNT(*) AS wins
            FROM matches
            WHERE winner IS NOT NULL
            GROUP BY winner
            ORDER BY wins DESC
            LIMIT 1
        """, None)

    if "highest total score" in q:
        return ("""
            SELECT match_id, batting_team, MAX(total_score) as score FROM (
                SELECT match_id, batting_team, SUM(runs_total) as total_score
                FROM deliveries
                GROUP BY match_id, inning, batting_team
            )
        """, None)

    if "matches played in" in q:
        city = q.split("in")[-1].strip().title()
        return ("SELECT match_id, date, team1, team2, venue FROM matches WHERE city = :city", {"city": city})

    if "who scored the most runs" in q:
        return ("""
            SELECT striker AS player, SUM(runs_batter) AS total_runs
            FROM deliveries
            GROUP BY striker
            ORDER BY total_runs DESC
            LIMIT 1
        """, None)

    if "most wickets" in q:
        return ("""
            SELECT bowler, COUNT(*) AS wickets
            FROM deliveries
            WHERE wicket_kind IS NOT NULL
            GROUP BY bowler
            ORDER BY wickets DESC
            LIMIT 1
        """, None)

    if "virat kohli" in q and "batting" in q:
        return ("""
            SELECT striker AS player, SUM(runs_batter) AS runs, COUNT(*) AS balls_faced,
                   ROUND(1.0 * SUM(runs_batter) / COUNT(*), 2) AS strike_rate
            FROM deliveries
            WHERE striker LIKE '%Kohli%'
            GROUP BY striker
        """, None)

    if "average first innings score" in q:
        return ("""
            SELECT ROUND(AVG(total_score), 2) AS avg_first_innings_score FROM (
                SELECT match_id, inning, SUM(runs_total) AS total_score
                FROM deliveries
                WHERE inning = 1
                GROUP BY match_id, inning
            )
        """, None)

    if "venue has the highest scoring matches" in q:
        return ("""
            SELECT m.venue, AVG(total_score) as avg_score FROM (
                SELECT match_id, inning, SUM(runs_total) as total_score
                FROM deliveries
                GROUP BY match_id, inning
            ) AS scores
            JOIN matches m ON m.match_id = scores.match_id
            GROUP BY m.venue
            ORDER BY avg_score DESC
            LIMIT 1
        """, None)

    if "centuries" in q:
        return ("""
            SELECT striker AS player, match_id, SUM(runs_batter) AS runs
            FROM deliveries
            GROUP BY match_id, striker
            HAVING runs >= 100
            ORDER BY runs DESC
        """, None)

    return None, None

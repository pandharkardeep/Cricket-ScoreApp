import requests
from tabulate import tabulate

def get_score_info(score, key):
    return score.get(key, 0)

def fetch_cricket_scores():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "74b10f24c9msh9fd947632f86905p187aebjsne3e91483531a"  # Replace with your RapidAPI key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    #print(data)
    matches = data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']
    #print(matches)
    for match in matches:
        table = []
       # print(match)
        table.append(["Match Description", f"{match['matchInfo']['matchDesc']} , {match['matchInfo']['team1']['teamName']} vs {match['matchInfo']['team2']['teamName']}"])
        table.append(["Match Details", ""])
        table.append(["Series Name", match['matchInfo']['seriesName']])
        table.append(["Match Format", match['matchInfo']['matchFormat']])
        table.append(["Result", match['matchInfo']['status']])
        #print(f"{match['matchInfo']['team1']['teamName']}", f"{match['matchScore']['team1Score']['inngs1']['runs']}/{match['matchScore']['team1Score']['inngs1']['wickets']} in {match['matchScore']['team1Score']['inngs1']['overs']} overs")
        
        team1_name = match['matchInfo']['team1']['teamName']
        team1_score = match.get('matchScore', {}).get('team1Score', {}).get('inngs1', {})
        team1_runs = get_score_info(team1_score, 'runs')
        team1_wickets = get_score_info(team1_score, 'wickets')
        team1_overs = get_score_info(team1_score, 'overs')
        table.append([team1_name, f"{team1_runs}/{team1_wickets} in {team1_overs} overs"])

        # Team 2 data
        team2_name = match['matchInfo']['team2']['teamName']
        team2_score = match.get('matchScore', {}).get('team2Score', {}).get('inngs1', {})
        team2_runs = get_score_info(team2_score, 'runs')
        team2_wickets = get_score_info(team2_score, 'wickets')
        team2_overs = get_score_info(team2_score, 'overs')
        table.append([team2_name, f"{team2_runs}/{team2_wickets} in {team2_overs} overs"])
       
        headers = ["Key", "Value"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print("\n")

fetch_cricket_scores()
from db_connection import matches_collection, teams_collection
from funcions import check_string, check_number, check_array, check_date, check_bool

def create_match():
    teams = list(teams_collection.find())

    for num, team in enumerate(teams, start=1):
        print(f"{num}. {team["name"]}")

    team_num = check_number("Select team number to update: ", is_empty=False)

    if team_num is None:
        print("Cancelled")
        return
    
    index = team_num - 1
    chosen = teams[index]
    team_id = chosen["_id"]
    
    date = check_date("Date: ", is_empty = False)
    if date is None:
        print("Cancelled")
        return
    
    opponent = check_string("Opponent: ", is_empty = False)
    if opponent is None:
        print("Cancelled")
        return
    
    home = check_bool("Home (Y/N): ", is_empty = False)
    if home is None:
        print("Cancelled")
        return
    
    score_team = check_number("Team score: ", is_empty=True)
    if score_team is None:
        print("Cancelled")
        return
    
    score_opponent = check_number("Opponent score: ", is_empty=True)
    if score_team is None:
        print("Cancelled")
        return
    
    match_result = ""
    
    if score_team > score_opponent:
        match_result = "win"
    elif score_team < score_opponent:
        match_result = "loss"
    else:
        match_result = "draw"
    
    new_match = {
        "team_id": team_id,
        "date": date,
        "opponent": opponent,
        "home": home,
        "score": {
            "team": score_team,
            "opponent": score_opponent
        },
        "result": match_result
    }

    insert_result = matches_collection.insert_one(new_match)
    print("New match is successfully created: {insert_result.inserted_id}")

def read_match():
    matches = matches_collection.find()
    for match in matches:
        team = teams_collection.find_one({"_id": match["team_id"]})
        team_name = team["name"]
        print(f"""
            Team:           {team_name} 
            Match Date:     {match["date"]}
            Opponent:       {match["opponent"]}
            Home:           {match["home"]}
            Score:          {match["score"]["team"]} - {match["score"]["opponent"]}
            Result:         {match["result"]}
            """)

def update_match():
    matches = list(matches_collection.find())

    for num, match in enumerate(matches, start=1):
        team = teams_collection.find_one({"_id": match["team_id"]})
        team_name = team["name"]
        print(f"{num}. {team_name} {match["score"]["team"]} - {match["score"]["opponent"]} {match["opponent"]}")

    match_num = check_number("Select match number to update: ", is_empty=False)
    index = match_num - 1
    chosen = matches[index]

    print("Empty value = unchanged \n")

    updated_date = check_date("New date: ", is_empty=True)
    if updated_date == "":
        updated_date = chosen["date"]

    updated_opponent = check_string("New opponent: ", is_empty=True)
    if updated_opponent == "":
        updated_opponent = chosen["opponent"]

    updated_home = check_bool("Home (Y/N): ", is_empty=True)
    if updated_home == "":
        updated_home = chosen["home"]

    updated_score_team = check_number("Team score: ", is_empty=True)
    if updated_score_team == "":
        updated_score_team = chosen["score"]["team"]

    updated_score_opponent = check_number("Team opponent: ", is_empty=True)
    if updated_score_opponent == "":
        updated_score_opponent = chosen["score"]["opponent"]

    match_result = ""
    
    if updated_score_team > updated_score_opponent:
        match_result = "win"
    elif updated_score_team < updated_score_opponent:
        match_result = "loss"
    else:
        match_result = "draw"

    matches_collection.update_one(
        {"_id": chosen["_id"]},
        {"$set" : {
            "team_id": chosen["team_id"],
            "date": updated_date,
            "opponent": updated_opponent,
            "home": updated_home,
            "score": {
                "team": updated_score_team,
                "opponent": updated_score_opponent
            },
            "result": match_result
        }}
    )

    print("Selected match updated!")

def delete_match():
    matches = list(matches_collection.find())

    for num, match in enumerate(matches, start=1):
        team = teams_collection.find_one({"_id": match["team_id"]})
        team_name = team["name"]
        print(f"{num}. {team_name} {match["score"]["team"]} - {match["score"]["opponent"]} {match["opponent"]}")

    match_num = check_number("Select match number to delete: ", is_empty=False)
    index = match_num - 1
    chosen = matches[index]

    delete_result = matches_collection.delete_one({"_id": chosen["_id"]})
    if delete_result.deleted_count == 1:
        print("Deletion was successful")
    else:
        print("Unexpected Error Occured")
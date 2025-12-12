from db_connection import teams_collection, matches_collection
from funcions import check_array, check_number, check_string

def create_team():
    name = check_string("Team name: ", is_empty = False)
    if name is None:
        print("Cancelled")
        return
    
    league = check_string("League: ", is_empty = False)
    if league is None:
        print("Cancelled")
        return
    
    founded = check_number("Founded: ", is_empty = False)
    if founded is None:
        print("Cancelled")
        return
    
    city = check_string("City: ", is_empty = False)
    if city is None:
        print("Cancelled")
        return
    
    championships = check_array("Championships (separate values with commas): ", is_empty=True)
    if championships is None:
        print("Cancelled")
        return
    
    new_team = {
        "name": name,
        "league": league,
        "founded": founded,
        "city": city,
        "championships": championships
    }

    insert_result = teams_collection.insert_one(new_team)
    print("New team is successfully created: {insert_result.inserted_id}")

def read_team():
    teams = teams_collection.find()
    for team in teams:
        print(f"""
            Name: {team["name"]} 
            League: {team["league"]}
            Founded: {team["founded"]}
            City: {team["city"]}
            Championships: {team["championships"]}
            """)

def update_team():
    teams = list(teams_collection.find())

    for num, team in enumerate(teams, start=1):
        print(f"{num}. {team["name"]}")

    team_num = check_number("Select team number to update: ", is_empty=False)
    index = team_num - 1
    chosen = teams[index]

    print("Empty value = unchanged \n")

    updated_name = check_string("New name: ", is_empty=True)
    if updated_name is None:
        print("Cancelled")
        return
    if updated_name == "":
        updated_name = chosen["name"]

    updated_league = check_string("New league: ", is_empty=True)
    if updated_league is None:
        print("Cancelled")
        return
    if updated_league == "":
        updated_league = chosen["league"]

    updated_founded = check_number("New founded: ", is_empty=True)
    if updated_founded is None:
        print("Cancelled")
        return
    if updated_founded == "":
        updated_founded = chosen["founded"]

    updated_city = check_string("New city: ", is_empty=True)
    if updated_city is None:
        print("Cancelled")
        return
    if updated_city == "":
        updated_city = chosen["city"]

    updated_championships = check_array("New array: ", is_empty=True)
    if updated_championships is None:
        print("Cancelled")
        return
    if updated_championships == "":
        updated_championships = chosen["championships"]

    teams_collection.update_one(
        {"_id": chosen["_id"]},
        {"$set" : {
            "name": updated_name,
            "league": updated_league,
            "founded": updated_founded,
            "city": updated_city,
            "championships": updated_championships
        }}
    )

    print("Selected team updated!")

def delete_team():
    teams = list(teams_collection.find())

    for num, team in enumerate(teams, start=1):
        print(f"{num}. {team["name"]}")

    team_num = check_number("Select team number to delete: ", is_empty=False)
    index = team_num - 1
    chosen = teams[index]

    delete_result = teams_collection.delete_one({"_id": chosen["_id"]})
    delete_matches = matches_collection.delete_many({"team_id": chosen["_id"]})

    if delete_result.deleted_count == 1 and delete_matches.deleted_count == 1:
        print("Deletion was successful, all the matches were deleted too.")
    else:
        print("Unexpected Error Occured")


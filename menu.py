from teams import create_team, read_team, update_team, delete_team
from matches import create_match, read_match, update_match, delete_match

def menu():
    while True:
        print("""
            Hey, select what you want to do (select number):
            
            1. Add a team
            2. View all existing teams
            3. Update existing team
            4. Delete existing team
            
            5. Add a match
            6. View all matches
            7. Update existing match
            8. Delete existing match
              
            "q" to go back
            """)
        
        choice = input("Choice : ")

        match choice:
            case "1":
                create_team()
            case "2":
                read_team()
            case "3":
                update_team()
            case "4":
                delete_team()
            case "5":
                create_match()
            case "6":
                read_match()
            case "7":
                update_match()
            case "8":
                delete_match()
            case "q":
                print("Exiting")
                break
            case _:
                print("Unknown input")

if __name__ == "__main__":
    menu()
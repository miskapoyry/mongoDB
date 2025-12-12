from datetime import datetime

def check_string(answer: str, is_empty: bool):
    while True:
        checked = input(answer).strip()

        if checked == "q":
            return None
        
        if not checked and not is_empty:
            print("Answer cannot be empty")
            continue

        return checked

def check_number(answer: int, is_empty: bool):
    while True:
        checked = input(answer).strip()

        if checked == "q":
            return None
        
        if not checked and not is_empty:
            print("Answer cannot be empty")
            continue
        
        if is_empty and checked == "":
            return ""
        
        if not checked.isnumeric():
            print("Value has to be a number...")
            continue

        return int(checked)
    
def check_array(answer: str, is_empty: bool):
    while True:
        checked = input(answer).strip()

        if checked == "q":
            return None
        
        if not checked:
            return []

        try:
            championships = [int(x) for x in checked.split(",")]
            return championships
        except ValueError:
            print("Values must be numeric and separated by commas")
            continue

def check_date(answer: str, is_empty:bool):
    while True:
        checked = input(answer).strip()

        if checked == "q":
            return None

        if is_empty and checked == "":
            return ""
        
        try:
            formatted = datetime.strptime(checked, "%Y-%m-%d")
            return formatted
        except ValueError:
            print("Not correct format. Make sure YYYY-MM-DD.")

def check_bool(answer:str, is_empty:bool):
    while True:
        checked = input(answer).strip()

        if checked == "q":
            return None
        
        if checked.lower() == "y":
            return True
        elif checked.lower() == "n":
            return False
        else:
            print("Answer only with Y/N...")
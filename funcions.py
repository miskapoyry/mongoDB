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
        except ValueError():
            print("Values must be numeric and separated by commas")
            continue
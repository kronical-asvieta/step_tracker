import datetime
import csv

current_date = datetime.date.today()

def load_data():
    with open('data.csv', newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def update_data(rows):
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['date', 'steps'])
        writer.writeheader()
        writer.writerows(rows)

def print_steps(steps):
    if steps == 1:
        return "1 step"
    elif steps >= 0:
        return f"{steps} steps"
    else:
        return f"{steps} steps.. I don't even know how you did that"


class Read:
    @staticmethod
    def full_stat():
        rows = load_data()
        for row in rows:
            print(f"Date: {row['date']}; Steps: {row['steps']}")

    @staticmethod
    def highest():
        rows = load_data()
        current_max = None
        for row in rows:
            if current_max is None or int(row['steps']) > current_max:
                current_max = int(row['steps'])
        
        print(f"Highest step count: {print_steps(current_max)}")

    @staticmethod
    def lowest():
        rows = load_data()
        current_min = None
        for row in rows:
            if current_min is None or int(row['steps']) < current_min:
                current_min = int(row['steps'])
        
        print(f"Lowest step count: {print_steps(current_min)}")

    @staticmethod
    def show_date():
        entered_date = input("Enter the date you're looking for: ")
        rows = load_data()
        for row in rows:
            if row['date'] == entered_date:
                print(f"{entered_date}'s step count: {print_steps(row['steps'])}")

class Write:
    @staticmethod
    def write_steps():
        enter_type = input("Enter date (today: t / custom date): ")

        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            if enter_type == "t" or enter_type == "today":
                inputted_steps = int(input("Enter step count: "))
                writer.writerow([current_date, inputted_steps])
            else:
                #from datetime import datetime

                try:
                    datetime.datetime.strptime(enter_type, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Use yyyy-mm-dd.")
                    return

                inputted_steps = int(input("Enter step count: "))
                rows = load_data()
                for row in rows:
                    if row['date'] == enter_type:
                        print(f"Replaced {row['date']}'s {print_steps(row['steps'])} steps with {print_steps(inputted_steps)}.")
                        row['steps'] = inputted_steps
                        update_data(rows)
                        return
                writer.writerow([enter_type, inputted_steps])
    
    @staticmethod
    def remove_steps():
        inputted_date = input("Enter the date you'd like to remove the steps of: ")

        rows = load_data()
        updated_rows = [row for row in rows if row['date'] != inputted_date]

        if len(updated_rows) == len(rows):
            print("Date not found in the database")
            return

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['date', 'steps'])
            writer.writeheader()
            writer.writerows(updated_rows)
        
        print(f"Removed entry for {inputted_date}")
    
    @staticmethod
    def modify_steps():
        inputted_date = input("Enter the date you'd like to modify the steps of: ")
        inputted_steps = int(input("Enter the new amount of steps: "))

        rows = load_data()
        for row in rows:
            if row['date'] == inputted_date:
                print(f"Replaced {row['date']}'s {print_steps(row['steps'])} with {print_steps(inputted_steps)}.")
                row['steps'] = inputted_steps
                update_data(rows)
                return
        
        print(f"\"{inputted_date}\" not found in the database")

def display_help():
    print("\nm:  Modifies a step count")
    print("    > Enter the date in the yyyy-mm-dd format and then the new step count (separated by a space)")
    print("r:  Removes a step count")
    print("    > Enter the date in the yyyy-mm-dd format")
    print("s:  Shows a specific date's step count")
    print("    > Enter the date in the yyyy-mm-dd format")
    print("w:  Writes a new step count into the statistics")
    print("    > Enter just the step count\n")
    print("h:  Displays this list")
    print("q:  Exits the program\n")
    print("hi: Displays your current highest recorded step count")
    print("lo: Displays your current lowest recorded step count")
    print("ls: Displays the full available stats\n")

display_help()

user_input = input("> ")

while user_input != "q":
    if user_input == "h":
        display_help()
    elif user_input == "w":
        Write.write_steps()
    elif user_input == "ls":
        Read.full_stat()
    elif user_input == "r":
        Write.remove_steps()
    elif user_input == "m":
        Write.modify_steps()
    elif user_input == "hi":
        Read.highest()
    elif user_input == "lo":
        Read.lowest()
    elif user_input == "s":
        Read.show_date()
    else:
        print("Unknown command. Enter 'h' for help")

    user_input = input("> ")
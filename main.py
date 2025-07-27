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


class Read:
    @staticmethod
    def full_stat():
        rows = load_data()
        for row in rows:
            print(f"Date: {row['date']}; Steps: {row['steps']}")

class Write:
    @staticmethod
    def write_steps():
        inputted_steps = int(input("Enter today's step count: "))

        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([current_date, inputted_steps])
    
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
                print(f"Replaced {row['date']}'s {row['steps']} steps with {inputted_steps}.")
                row['steps'] = inputted_steps

                update_data(rows)

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
    else:
        print("Unknown command. Enter 'h' for help")

    user_input = input("> ")
import datetime
import csv

date = datetime.date.today()

class Read:
    @staticmethod
    def full_stat():
        with open('data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                print(row)

class Write:
    @staticmethod
    def write_steps():
        inputted_steps = int(input("Enter today's step count: "))
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([date, inputted_steps])

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
    if user_input == "w":
        Write.write_steps()
    user_input = input("> ")
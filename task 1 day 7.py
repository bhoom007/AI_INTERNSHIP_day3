nameofperson = input("Enter your name: ")
dailygoal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"{nameofperson} - {dailygoal}\n")

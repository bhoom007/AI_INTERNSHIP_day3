import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  

    for row in reader:
        if row[2] == "Pass":   
            print(row[0])     

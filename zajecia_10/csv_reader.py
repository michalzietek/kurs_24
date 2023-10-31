import csv

with open("file.csv") as file:
    data = csv.reader(file)
    for line in data:
        print(line)

import sys
import os
import csv

class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.input_data = []

    def read_file_from_source(self):
        if os.path.isfile(self.input_file):
            with open(self.input_file) as file:
                reader = csv.reader(file)
                for row in reader:
                    self.input_data.append(row)
        else:
            print(os.listdir(self.input_file))
            print("Nie jest plikiem")

    def change_data(self):
        for change in self.changes:
            changes_list = change.split(",")
            self.input_data[int(changes_list[0])][int(changes_list[1])] = changes_list[2]

    def write_data_to_file(self):
        with open(self.output_file, mode="???") as file:
            writer = csv.writer(file)
            writer.writerows(self.input_data)


input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]
file_handler = FileHandler(input_file, output_file, changes)
file_handler.read_file_from_source()
file_handler.change_data()
print("hehe")

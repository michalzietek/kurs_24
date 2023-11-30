import pickle
from abc import abstractmethod

class FileHandler:
    def __init__(self, arguments_in_console):
        self.input_file = arguments_in_console[1]
        self.output_file = arguments_in_console[2]
        self.changes = arguments_in_console[3:]
        self.data = None

    @abstractmethod
    def read_data_from_file(self):
        raise NotImplementedError("Niestety, nie masz zaimplementowanej obsługi rozszerzenia tego pliku.")

    @abstractmethod
    def write_data_to_file(self):
        raise NotImplementedError("Niestety, nie masz zaimplementowanej obsługi rozszerzenia tego pliku.")

    def change_data_accordingly_to_changes(self):
        for change in self.changes:
            x_value, y_value, new_field = change.split(",")
            print(change)
            self.data[int(x_value)][int(y_value)] = new_field


class TxtFileHandler(FileHandler):
    def read_data_from_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            for line in file:
                temporary_data.append(line.split(","))
        self.data = temporary_data

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            for line in self.data:
                file.write(",".join(line))


class PickleFileHandler(FileHandler):
    def read_data_from_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def write_data_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.data, file)

import json


class FileHandler:
    def __init__(self, history_file, warehouse_file):
        self.warehouse_file = warehouse_file
        self.history_file = history_file
        self.warehouse, self.saldo = self.read_data_from_warehouse_file()
        self.history = self.read_data_from_history_file()

    def read_data_from_warehouse_file(self):
        with open(self.warehouse_file) as file:
            warehouse_temporary = json.loads(file.read())
            return warehouse_temporary.get("magazyn"), warehouse_temporary.get("saldo")

    def read_data_from_history_file(self):
        with open(self.history_file) as file:
            history_data = json.loads(file.read())
            return history_data

    def write_data_to_warehouse_file(self):
        with open(self.warehouse_file, mode="w+") as file:
            file.write(json.dumps({"saldo": self.saldo, "magazyn": self.warehouse}))

    def change_saldo(self, new_saldo):
        self.saldo += int(new_saldo)

    def add_new_input_to_history(self, new_input):
        self.history.append(new_input)

    def write_data_to_history_file(self):
        with open(self.history_file, mode="w+") as file:
            file.write(json.dumps(self.history))

    def write_data_to_history_file_without_update(self, new_input):
        #tutaj uwaga! pliki json muszą stringi mieć w podwójnym cudzysłowie- " a nie pojedynczym -' .
        # jesli sa w pojedynczym wystarczy zrobic funkcje replace
        with open(self.history_file, mode="a") as file:
            file.write(json.dumps(f",{new_input}"))


file_handler = FileHandler(history_file="history.json", warehouse_file="warehouse.json")
print(file_handler)
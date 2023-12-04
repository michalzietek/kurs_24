from file_handler import FileHandler
import sys

class Manager:
    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)






manager = Manager()


@manager.assign("zmien_saldo")
def change_saldo(manager):
    warehouse_file = sys.argv[1]
    file_handler = FileHandler(warehouse_file=warehouse_file, history_file="history.json")
    file_handler.change_saldo(sys.argv[2])
    file_handler.add_new_input_to_history(sys.argv[3])
    file_handler.write_data_to_warehouse_file()
    # file_handler.write_data_to_history_file()
    file_handler.write_data_to_history_file_without_update(sys.argv[3])


@manager.assign("pokaz_siebie")
def show_yourself(manager):
    print("Pokazales siebie")
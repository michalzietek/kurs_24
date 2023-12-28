from zajecia_24.accountant.file_handler import FileHandler


class Manager(FileHandler):

    def __init__(self, history_file, magazyn_and_saldo_file):
        self.history_file = history_file
        self.magazyn_and_saldo_file = magazyn_and_saldo_file
        print("zainicjalizowalem obiekt")
        self.history = self.load_history(history_file)
        self.saldo, self.magazyn = self.load_saldo_and_magazyn(magazyn_and_saldo_file)
        self.actions = {}

    def assign(self, name):
        def wrapper(function):
            self.actions[name] = function
        return wrapper

    def execute(self, name):
        if not name in self.actions:
            print("Niestety nie ma takiej akcji")
        else:
            self.actions[name](self)


manager = Manager(history_file="accountant/history.txt", magazyn_and_saldo_file="accountant/warehouse.txt")

@manager.assign("Saldo")
def change_saldo(manager: Manager):
    amount = float(input("Podaj kwotę, którą chcesz dodać lub odjąć z konta"))
    manager.saldo += amount
    manager.history.append(f"Wykonano instrukcję saldo, zasilono {amount}")
    manager.save_saldo_and_magazyn_to_file(file=manager.magazyn_and_saldo_file,
                                           saldo=manager.saldo,
                                           magazyn=manager.magazyn)
    manager.save_history(file=manager.history_file, history=manager.history)

@manager.assign("Sprzedaz")
def sell_item(manager: Manager):
    print(manager.magazyn)
    product = input("Podaj nazwę produktu: ")
    # TODO zmienić na floaty bo np kg
    amount = int(input("Podaj ilość, którą chcesz sprzedać: "))
    product_found = False
    # najpierw sprawdzmy czy mamy towar
    for item, item_details in manager.magazyn.items():
        if product == item:
            item_details["ilosc"] -= amount
            manager.saldo += (item_details["cena"] * amount)
            product_found = True
            manager.history.append(f"Sprzedano {product} w ilości {amount}")
            break
    if not product_found:
        manager.history.append(f"Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie")
    manager.save_saldo_and_magazyn_to_file(file=manager.magazyn_and_saldo_file,
                                           saldo=manager.saldo,
                                           magazyn=manager.magazyn)
    manager.save_history(file=manager.history_file, history=manager.history)


@manager.assign("Historia")
def lookup_for_data(manager: Manager):
    # TODO jak value bedzie wieksze od naszej listy to wyprintować długość listy len()
    value_from = input("Podaj początkowy zakres")
    value_to = input("Podaj końcowy zakres")
    if not value_to and not value_from:
        print(manager.history)
    elif value_from and not value_to:
        print(manager.history[value_from:])
    manager.save_saldo_and_magazyn_to_file(file=manager.magazyn_and_saldo_file,
                                           saldo=manager.saldo,
                                           magazyn=manager.magazyn)
    manager.save_history(file=manager.history_file, history=manager.history)
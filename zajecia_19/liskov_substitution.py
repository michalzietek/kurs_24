from abc import abstractmethod


class Engine:
    def __init__(self):
        self.power = "150hp"
        self.volume = "2.0l"
        self.engine_type = "Diesel"


    @abstractmethod
    def load_fuel(self):
        print("Napełniłem bak paliwa")


class OilEngineDuty:
    @abstractmethod
    def change_oil(self):
        pass


class DieselEngine(Engine, OilEngineDuty):
    def change_oil(self):
        print("Zmieniłem olej")

    def load_fuel(self):
        print("Zatankowałem diesla")


class ElectricEngine(Engine):

    def load_fuel(self):
        pass



class Bird:
    @abstractmethod
    def move(self):
        pass

class Pinguin(Bird):
    def move(self):
        print("Ja chodzę")


class Pigeon(Bird):
    def move(self):
        print("Ja latam")
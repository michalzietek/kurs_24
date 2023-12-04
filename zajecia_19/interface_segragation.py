from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def run_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class ElectricMaintenance(ABC):

    @abstractmethod
    def utilize_battery(self):
        pass

    @abstractmethod
    def plug_in(self):
        pass

class OilMaintenance(ABC):

    @abstractmethod
    def change_oil(self):
        pass


class ElectricEngine(Engine, ElectricMaintenance):
    def run_engine(self):
        pass

    def stop_engine(self):
        pass

    def utilize_battery(self):
        pass

    def plug_in(self):
        pass



class OilEngine(Engine, OilMaintenance):
    def run_engine(self):
        pass

    def stop_engine(self):
        pass

    def change_oil(self):
        pass



class Bird:
    @abstractmethod
    def move(self):
        pass


class FlyingBird:
    def fly(self):
        print("Ja latam")


class Pinguin(Bird):
    def move(self):
        print("Ja chodzę")


class Pigeon(Bird, FlyingBird):
    pass


pinguin = Pinguin()
pigeon = Pigeon()
pigeon.fly()
from abc import ABC, abstractmethod
#brzydki przyklad - nie korzystac
# class PetrolEngine:
#     def start(self):
#         return "Odpalam silnik spalinowy"
#
# class Car:
#     def __init__(self):
#         self.engine = PetrolEngine()
#
#     def start(self):
#         return self.engine.start()
#


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass


class OilEngine(Engine):
    def start(self):
        return "Opdalam silnik spalinowy"


class ElectricEngine(Engine):
    def start(self):
        return "Odpalam silnik elektryczny"


class HydraulicEngine(Engine):
    pass


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        print(self.engine.start())


car = Car(OilEngine())
car.start()
electric_car = Car(ElectricEngine())
electric_car.start()
from abc import abstractmethod

class Zwierze:

    @abstractmethod
    def daj_glos(self):
        raise NotImplementedError

    def idz_spac(self):
        print("Poszedlem spac")

    @abstractmethod
    def powiedz_mi_gdzie_mieszkasz(self):
        raise NotImplementedError


class Lew(Zwierze):
    def daj_glos(self):
        print("Rawrrr")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam na sawannie")


class Delfin(Zwierze):
    def daj_glos(self):
        print(".......")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w wodzie")


class Pies(Zwierze):
    def daj_glos(self):
        print("Hau hau")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w domu na ziemi.")


class Kot(Zwierze):
    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w domu w legowisku.")

    def daj_glos(self):
        print("Miauu.")


pies = Pies()
delfin = Delfin()
lew = Lew()
lew.daj_glos()
pies.daj_glos()
delfin.daj_glos()
pies.idz_spac()
lew.idz_spac()
delfin.idz_spac()
kot = Kot()
kot.daj_glos()
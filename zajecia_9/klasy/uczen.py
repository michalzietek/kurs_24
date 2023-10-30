class Uczen:
    def __init__(self, imie="Jan", nazwisko="Nowak", oceny=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny

    def __repr__(self):
        return f"Uczeń o imieniu: {self.imie}, nazwisku: {self.nazwisko} i ocenach: {self.oceny}"

    def dodaj_ocene_dla_ucznia(self, ocena):
        self.oceny.append(ocena)


def dodaj_dwie_liczby(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba
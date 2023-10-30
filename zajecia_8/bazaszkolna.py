import sys

argumenty = sys.argv[1:]
koniec_programu = False
print("Witaj w naszej szkole, podaj opcję jaką chcesz wykonać.")

lista_uczniow = []
lista_nauczycieli = []
lista_wychowawcow = []


def znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika):
    print(argumenty)
    print("Kod do znalezienia danych z argumentow systemowych wsrod uczniow")

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

while not koniec_programu:
    wybrana_opcja = input("1. Dodaj ucznia\n2. Dodaj nauczyciela\n3. Dodaj wychowawce\n4. Koniec\n")
    if wybrana_opcja == "1":
        imie_input = input("Podaj imie ucznia: ")
        nazwisko_input = input("Podaj nazwisko ucznia: ")
        klasa_input = input("Podaj klase ucznia: ")
        nowy_uczen = Uczen(imie=imie_input, nazwisko=nazwisko_input, klasa=klasa_input)

    elif wybrana_opcja == "2":
        print("Dodajemy nauczyciela")
        pusty_input = False
        while not pusty_input:
            numer_klasy = input("Podaj kolejna klase")
            if numer_klasy == "":
                pusty_input = True
    elif wybrana_opcja == "3":
        print("Dodajemy wychowawce")
    elif wybrana_opcja == "4":
        print("koniec - wykonujemy operacje z argumentow systemowych")
        print(argumenty)
        dane_uzytkownika = argumenty[0]
        znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika)
        koniec_programu = True
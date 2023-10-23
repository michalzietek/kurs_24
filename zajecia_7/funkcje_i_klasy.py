baza_szkolna = {
    "1a": [{
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "oceny": [1, 2, 4]
        },
        {"imie": "Jan",
         "nazwisko": "Kowalski",
         "oceny": [2, 3, 5]
         }
        ]
}

# def znajdz_mojego_ucznia(klasa_ucznia, imie_ucznia, nazwisko_ucznia):
#     for numer_klasy, klasa in baza_szkolna.items():
#         if numer_klasy == klasa_ucznia:
#             for uczen in klasa:
#                 if imie_ucznia == uczen.get("imie") and nazwisko_ucznia == uczen.get("nazwisko"):
#                     return uczen
#     return None
#
# def zapytanie_uzytkownika_o_dane_ucznia():
#     klasa_ucznia = "1a"
#     imie_ucznia = "Michał"
#     nazwisko_ucznia = "Ziętkowski"
#     return (klasa_ucznia, imie_ucznia, nazwisko_ucznia)
#
#
# print("Witaj w programie do zarzadzania nasza szkola. Podaj co chcesz zrobić.")
# wybor_uzytkowniaka = input("1. Dodaj ocene uczniowi\n2. Dodaj ucznia\n3. Zmien wartosc u ucznia\n")
# if wybor_uzytkowniaka == "1":
#     klasa_ucznia, imie_ucznia, nazwisko_ucznia = zapytanie_uzytkownika_o_dane_ucznia()
#     uczen = znajdz_mojego_ucznia(klasa_ucznia=klasa_ucznia, imie_ucznia=imie_ucznia, nazwisko_ucznia=nazwisko_ucznia)
#     print(uczen)
#     for numer_klasy, klasa in baza_szkolna.items():
#         if klasa_ucznia == numer_klasy:
#             for uczen in klasa:
#                 if imie_ucznia == uczen.get("imie") and nazwisko_ucznia == uczen.get("nazwisko"):
#                     uczen["oceny"].append(int(ocena_ucznia))
#                     break
#             print("Nie ma takiego ucznia")
# elif wybor_uzytkowniaka == "2":
#     klasa_ucznia, imie_ucznia, nazwisko_ucznia = zapytanie_uzytkownika_o_dane_ucznia()
#     for numer_klasy, klasa in baza_szkolna.items():
#         if klasa_ucznia == numer_klasy:
#             baza_szkolna[klasa_ucznia] = {
#
#             }


def dodawanie_dwoch_liczb(pierwsza_liczba, druga_liczba, trzecia_liczba=10):
    return pierwsza_liczba + druga_liczba + trzecia_liczba


print(dodawanie_dwoch_liczb(5, 10))


class Uczen:
    def __init__(self, imie="Jan", nazwisko="Nowak", oceny=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny

    def __repr__(self):
        return f"Uczeń o imieniu: {self.imie}, nazwisku: {self.nazwisko} i ocenach: {self.oceny}"

    def dodaj_ocene_dla_ucznia(self, ocena):
        self.oceny.append(ocena)


uczen_michal = Uczen(imie="Michal", nazwisko="Zietkowski", oceny=[1, 3, 3, 4])
uczen_piotr = Uczen(imie="Piotr", nazwisko="Nazwisko", oceny=[1, 3, 3, 1])


class BazaSzkolna:
    def __init__(self, lista_uczniow):
        self.lista_uczniow = lista_uczniow

    def znajdz_ucznia(self, imie, nazwisko):
        for uczen in self.lista_uczniow:
            if uczen.imie == imie and uczen.nazwisko == nazwisko:
                return uczen
        return None

def znajdz_mojego_ucznia(klasa_ucznia, imie_ucznia, nazwisko_ucznia):
    for numer_klasy, klasa in baza_szkolna.items():
        if numer_klasy == klasa_ucznia:
            for uczen in klasa:
                if imie_ucznia == uczen.get("imie", "domyslne_imie") and nazwisko_ucznia == uczen.get("nazwisko"):
                    return uczen
    return None



baza_szkolna = BazaSzkolna(lista_uczniow=[uczen_piotr, uczen_michal])



uczen = Uczen()
print(uczen)














# print(uczen_michal)
# uczen_michal.dodaj_ocene_dla_ucznia(2)
# print(uczen_michal)
# print(uczen_piotr)

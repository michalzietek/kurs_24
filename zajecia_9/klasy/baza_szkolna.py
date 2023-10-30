
class BazaSzkolna:
    def __init__(self, lista_uczniow):
        self.lista_uczniow = lista_uczniow

    def znajdz_ucznia(self, imie, nazwisko):
        for uczen in self.lista_uczniow:
            if uczen.imie == imie and uczen.nazwisko == nazwisko:
                return uczen
        return None


def znajdz_mojego_ucznia(klasa_ucznia, imie_ucznia, nazwisko_ucznia):
    # for numer_klasy, klasa in baza_szkolna.items():
    #     if numer_klasy == klasa_ucznia:
    #         for uczen in klasa:
    #             if imie_ucznia == uczen.get("imie", "domyslne_imie") and nazwisko_ucznia == uczen.get("nazwisko"):
    #                 return uczen
    return None

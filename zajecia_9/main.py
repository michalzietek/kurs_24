from zajecia_9.klasy.uczen import Uczen, dodaj_dwie_liczby
from zajecia_9.klasy.baza_szkolna import BazaSzkolna, znajdz_mojego_ucznia

uczen_michal = Uczen(imie="Michal", nazwisko="Zietkowski", oceny=[1, 3, 3, 4])
uczen_piotr = Uczen(imie="Piotr", nazwisko="Nazwisko", oceny=[1, 3, 3, 1])
baza_szkolna = BazaSzkolna(lista_uczniow=[uczen_piotr, uczen_michal])
baza_szkolna.znajdz_ucznia("Michal", "Zietkowski")
znajdz_mojego_ucznia("1a", "Michal", "Zietkowski")
print(dodaj_dwie_liczby(1, 2))
print(uczen_michal)
print(uczen_piotr)

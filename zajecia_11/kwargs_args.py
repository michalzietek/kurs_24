def dodawanie_kilku_liczb(*args):
    suma_liczb = 0
    for liczba in args: #args to lista
        suma_liczb += liczba
    return suma_liczb


def utworz_mojego_ucznia(imie, nazwisko, **kwargs):
    slownik_z_kwargsow = {}
    for key, value in kwargs.items(): #kwargs to slownik
        slownik_z_kwargsow[key] = value
    return {
        "imie": imie,
        "nazwisko": nazwisko,
        **slownik_z_kwargsow
    }

def wypisz_kwargs_i_args(*args, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    for item in args:
        print(item)

print(dodawanie_kilku_liczb(1, 2, 3, 4, 5, 60))
print(dodawanie_kilku_liczb(2, 5))
print(utworz_mojego_ucznia("Michal", "Zietkowski"))
print(utworz_mojego_ucznia("Michal", "Zietkowski", plec="mezczyzna", wiek=27))
print(utworz_mojego_ucznia("Michal", "Zietkowski", plec="mezczyzna", wiek=27, oceny=[1,2,4]))
print(utworz_mojego_ucznia(plec="mezczyzna", wiek=27, oceny=[1,2,4], imie="Michal", nazwisko="Zietkowski"))
wypisz_kwargs_i_args(5, 3, 2, 5, 3, imie="Michal", nazwisko="Zietkowski")
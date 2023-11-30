import time

def dodawanie(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba

def odejmowanie(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba - druga_liczba

def oblicz_wynik(dzialanie, pierwsza_liczba, druga_liczba):
    if dzialanie == "dodawanie":
        return dodawanie(pierwsza_liczba, druga_liczba)
    elif dzialanie == "odejmowanie":
        return odejmowanie(pierwsza_liczba, druga_liczba)

# print(oblicz_wynik("dodawanie", 1, 1))
# print(oblicz_wynik("odejmowanie", 1, 1))


def sprawdz_liczbe():
    print("Sprawdzilem liczbe")


# przechowywalnia_sprawdzenia_liczby = sprawdz_liczbe
# przechowywalnia_sprawdzenia_liczby()

pracownicy = ["Jan", "Adam", "Andrzej", "Zbigniew"]
uzytkownicy = ["Jan Bednarek", "Adam Małysz", "Robert Kubica"]

def wyswietl_liczby(function):
    print("Wyswietlilem liczby: 1, 2, 3, 4, 5")
    function()
    print("abxdefsdsfEC")

#wyswietl_liczby(sprawdz_liczbe)


def login_required(function):
    print("Sprawdzam czy jestem zalogowany")
    print("Jestem zalogowany")
    function()


def login_required_decorator(function):
    def wrapper():
        print("Sprawdzam czy jestem zalogowany")
        print("Jestem zalogowany")
        function()
        print("Zamykam sesję użytkownika")
    return wrapper


def sprawdz_liczbe_pracownikow():
    print(len(pracownicy))

@login_required_decorator
def wyswietl_wszystkich_uzytkownikow():
    print(uzytkownicy)

#login_required(sprawdz_liczbe_pracownikow)

#login_required(wyswietl_wszystkich_uzytkownikow)

wyswietl_wszystkich_uzytkownikow()

def timeit(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Program wykonał się w {execution_time}")
    return wrapper

@timeit
def wyswietl_mi_uzytkownikow():
    for user in uzytkownicy:
        print(user)

wyswietl_mi_uzytkownikow()

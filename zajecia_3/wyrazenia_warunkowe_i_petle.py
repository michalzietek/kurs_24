# moj_wiek = int(input("Podaj mi swoj wiek "))
# moje_wynagrodzenie = None
# if moj_wiek < 65 and moj_wiek > 18:
#     print(f"Twój wiek to: {moj_wiek} brakuje Ci {65 - int(moj_wiek)} do emerytury")
#     moje_wynagrodzenie = int(input("Podaj mi swoje wynagrodzenie"))
#     if moje_wynagrodzenie > 5000:
#         print("Zarabiasz ponad srednia krajowa")
#     else:
#         print("Zarabiasz mniej niż średnia")
#     print(f"Twoje wynagrodzenie to: {moje_wynagrodzenie}")
# elif moj_wiek < 18:
#     print("Powinienes zajac sie nauka")
# else:
#     print("Jesteś już na emeryturze, korzystaj z życia")
#     print("Utworz melodie")
# print(moje_wynagrodzenie)
# print("Zakonczylem program")

# moje_imie = "Michal"

# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)
# print(moje_imie)

# for {zmienna tworzona dla iteracji} in {jakiejs_struktury, ktora moze byc iterowalna}:
#     {instrukcje do wykonania}

# for number in range(5):
#     print(number)
#     print(moje_imie)
#
# imie_uzytkownika = input("Podaj mi swoje imię: ")
# litera = 20
# for litera in imie_uzytkownika:
#     print(litera)

# wiek_osoby_niepelnoletniej = int(input("Podaj mi swój wiek: "))
#
# while wiek_osoby_niepelnoletniej < 18:
#     print(f"Niestety, nie masz jeszcze 18 lat. Brakuje Ci {18-wiek_osoby_niepelnoletniej}")
#     wiek_osoby_niepelnoletniej += 1
#     if wiek_osoby_niepelnoletniej == 16:
#         print("Hurra możesz już jeździć autem.")
#         poczekaj_na_pelnoletnosc = input("Czy na pewno chcesz mieć 18 lat?")
#         if poczekaj_na_pelnoletnosc == "tak":
#             continue
#             print("Czyli chodzi o alkohol!")
#         else:
#             break
#
#
# print("Wyszedles po kilku latach")
# import sys
#
# wiek_uzytkownika = sys.argv[1]
# wyplata_uzytkownika = sys.argv[2]
# print(wiek_uzytkownika)
# print(wyplata_uzytkownika)
# print(sys.argv[3])
moj_wiek = 67
if moj_wiek < 65 and moj_wiek > 18:
    print("Mozesz pracowac")
elif moj_wiek > 65:
    print("Jestes na emeryturze")
elif moj_wiek < 18:
    print("Powinienes sie jeszcze uczyc")
else:
    print("Nie wpisales prawidlowo swojego wieku")

for numer in range(100):
    twoj_szczesliwy_numer = 7
    if numer != twoj_szczesliwy_numer:
        pass
    else:
        print("Znalazlem Twoj szczesliwy numer")
    print(numer)


# twoj_wiek = 12
#
# while twoj_wiek < 18:
#     print(twoj_wiek)
#     twoj_wiek += 1
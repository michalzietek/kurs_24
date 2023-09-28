#napisanie programu do obliczenia ile zostało nam do wieku emerytalnego
#jako dane użytkownika pobieramy Imię oraz rok urodzenia

#jako wyjscie powinnismy dostac wiadomosc czy jestesmy w wieku emerytalnym oraz jesli nie to ile zostalo nam lat do tego czasu
print("Witaj w naszym programie.\nDzisiaj obliczymy czy jesteś w wieku emerytalnym oraz ile Ci do niego ewentualnie brakuje")
imie = input("Podaj mi swoje imię ")
rok_urodzenia = int(input("Podaj mi swój rok urodzenia "))
obecny_rok = 2023
wiek_emerytalny = 65
wiek_uzytkownika = obecny_rok - rok_urodzenia

print(f"Twój wiek to {wiek_uzytkownika}, brakuje Ci {wiek_emerytalny - wiek_uzytkownika} do emerytury")

print("Twój wiek to {wiek_uzytkownika_do_wyswietlenia}, brakuje Ci {lata_do_emerytury} do emerytury".format(wiek_uzytkownika_do_wyswietlenia=wiek_uzytkownika,
                                                                                            lata_do_emerytury=wiek_emerytalny-wiek_uzytkownika))

#######################################################################################################################

'''
    Konwersja Temperatury:
     Przy użyciu zmiennych typu float,
     napisz program, który konwertuje temperaturę w stopniach Celsiusza na temperaturę w stopniach Fahrenheita.
     Stosuj wzór: Fahrenheit = (Celsius * 9/5) + 32.
'''
# print("Witaj w programie konwersji temperatury wyrazonej w Celsiusach do temperatury w Fahrenheitach")
#
# temperatura_w_celsiusach = float(input("Podaj nam temperaturę w Celsiusach: "))
#
# temperatura_w_fahrentaitach = (temperatura_w_celsiusach * 9/5) + 32
#
# print(f"Temperatura w Fahrenheitach wynosi: {temperatura_w_fahrentaitach}")


#######################################################################################################################

'''
    Dzielenie Bez Reszty: Zdefiniuj dwie zmienne typu int i oblicz wynik dzielenia pierwszej przez drugą bez uwzględniania reszty.
     Wyświetl wynik.
    dzielenie //
'''
# print("Witaj w naszym programie do obliczania wyniku dzielenia bez reszty.")
# pierwsza_liczba = float(input("Podaj liczbę, którą chcesz podzielić: "))
# druga_liczba = float(input("Podaj liczbę, przez którą chcesz podzielić: "))
#
# print(f"Twoja liczba całkowita z dzielenia wynosi: {int(pierwsza_liczba//druga_liczba)}")
# print(type(pierwsza_liczba))


#######################################################################################################################
print("Witaj w naszym programie do sprawdzania czy dany wyraz znajdue się w innym wyrazie")

pierwszy_wyraz = input("Podaj wyraz, który ma znaleźć się w drugim wyrazie: ")
drugi_wyraz = input("Podaj wyraz, w którym chcesz przeszukiwać: ")

czy_jest_podwyrazem = pierwszy_wyraz in drugi_wyraz

print(f"Odpowiedź brzmi: {czy_jest_podwyrazem}")

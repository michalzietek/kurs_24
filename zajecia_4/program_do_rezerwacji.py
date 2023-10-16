sala = [[False, False, False, False],
        [False, False, False, False]]

'''
Napisz program do zarządzania rezerwacją miejsc w kinie.
Kino ma określoną liczbę rzędów i miejsc w każdym rzędzie.
Twoim zadaniem jest stworzyć program, który umożliwia rezerwację miejsc dla widzów.
Każde miejsce może być zarezerwowane tylko raz, a każdy widz może zarezerwować maksymalnie jedno miejsce.

Program powinien umożliwiać dodawanie rezerwacji dla kolejnych widzów, aż do wyczerpania dostępnych miejsc lub do momentu,
gdy użytkownik zdecyduje się zakończyć rezerwacje (np. poprzez wprowadzenie specjalnej komendy).
/0 w paczkach to u nas moze byc jakies slowo

Jeśli próba zarezerwowania miejsca nie jest możliwa (np. miejsce jest już zajęte, nie istnieje, lub numer miejsca jest nieprawidłowy),
program powinien wyświetlić odpowiednią wiadomość o błędzie i kontynuować rezerwacje. # tutaj bedzie cos innego niz w paczkach

Po zakończeniu rezerwacji program powinien wyświetlić następujące informacje:

    Liczbę zarezerwowanych miejsc
    Procent dostępnych miejsc, które zostały zarezerwowane
    Numer rzędu, w którym jest najwięcej zarezerwowanych miejsc
    Liczbę zarezerwowanych miejsc w tym rzędzie

Program powinien również obsługiwać błędy, takie jak próba zarezerwowania nieprawidłowego numeru miejsca lub próba rezerwacji,
gdy nie ma już dostępnych miejsc.

od uzytkownika:
numer miejsca, ktore chce zarezerwowac

co powinnismy trzymac w naszym globalnym stanie?
- ilosc miejsc na sali oraz stan poszczegolnych miejsc (czy sa sprzedane?)
- ilosc miejsc juz sprzedanych
- ilosc miejsc sprzedanych w danym rzedzie
- ilosc rzedow
'''
print("Witaj w naszym systemie rezerwacji/sprzedaży biletów.")

ilosc_miejsc = 16
ilosc_rzedow = 2
ilosc_miejsc_sprzedanych_w_1_rzedzie = 0
ilosc_miejsc_sprzedanych_w_2_rzedzie = 0

koniec_programu = False

while not koniec_programu:
    print("Podaj co chcesz zrobić w naszym programie.\n"
          "1. Zrob rezerwacje miejsca\n"
          "2. Zakoncz program i wyswietl nam potrzebne informacje")
    wybor_menu = input("Wybierz opcję. ")
    if int(wybor_menu) == 1:
        rzad_uzytkownika = input("Podaj rzad, w którym chcesz zarezerwować miejsce ")
        if not int(rzad_uzytkownika) in range(1,3):
            print("Niestety nie mamy takie rzędu w naszym kinie.")
            continue
        miejsce_uzytkownika = input("Podaj miejsce ")
        if not int(miejsce_uzytkownika) in range(1,9):
            print("Niestety nie mamy takiego miejsca.")
            continue
        # if int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 1:
        #     if not rzad_1_miejsce_1:
        #         rzad_1_miejsce_1 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety to miejsce jest już zajęte")
        #         continue
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 2:
        #     if not rzad_1_miejsce_2:
        #         rzad_1_miejsce_2 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 3:
        #     if not rzad_1_miejsce_3:
        #         rzad_1_miejsce_3 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 4:
        #     if not rzad_1_miejsce_4:
        #         rzad_1_miejsce_4 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 5:
        #     if not rzad_1_miejsce_5:
        #         rzad_1_miejsce_5 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 6:
        #     if not rzad_1_miejsce_6:
        #         rzad_1_miejsce_6 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 7:
        #     if not rzad_1_miejsce_7:
        #         rzad_1_miejsce_7 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 8:
        #     if not rzad_1_miejsce_8:
        #         rzad_1_miejsce_8 = True
        #         ilosc_miejsc_sprzedanych_w_1_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 1:
        #     if not rzad_2_miejsce_1:
        #         rzad_2_miejsce_1 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 2:
        #     if not rzad_2_miejsce_2:
        #         rzad_2_miejsce_2 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 3:
        #     if not rzad_2_miejsce_3:
        #         rzad_2_miejsce_3 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 4:
        #     if not rzad_2_miejsce_4:
        #         rzad_2_miejsce_4 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 5:
        #     if not rzad_2_miejsce_5:
        #         rzad_2_miejsce_5 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 6:
        #     if not rzad_2_miejsce_6:
        #         rzad_2_miejsce_6 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 7:
        #     if not rzad_2_miejsce_7:
        #         rzad_2_miejsce_7 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        # else:
        #     if not rzad_2_miejsce_8:
        #         rzad_2_miejsce_8 = True
        #         ilosc_miejsc_sprzedanych_w_2_rzedzie += 1
        #     else:
        #         print("Niestety, to miejsce jest już zajęte")
        wybrane_miejsce = sala[int(rzad_uzytkownika)-1][int(miejsce_uzytkownika)-1]
        if not wybrane_miejsce:
            sala[int(rzad_uzytkownika) - 1][int(miejsce_uzytkownika) - 1] = True
    elif int(wybor_menu) == 2:
        koniec_programu = True

print("Zakonczylismy dzialanie programu! Oto statystyki z twojej sprzedaży: ")
print(f"Ilość sprzedanych biletów to: {ilosc_miejsc_sprzedanych_w_1_rzedzie + ilosc_miejsc_sprzedanych_w_2_rzedzie}")
print(f"Procentowo jest to: {(ilosc_miejsc_sprzedanych_w_1_rzedzie + ilosc_miejsc_sprzedanych_w_2_rzedzie)/ilosc_miejsc}")
if ilosc_miejsc_sprzedanych_w_1_rzedzie > ilosc_miejsc_sprzedanych_w_2_rzedzie:
    print(f"Najwięcej miejsc sprzedaliśmy w 1 rzędzie. Było to: {ilosc_miejsc_sprzedanych_w_1_rzedzie} biletów")
elif ilosc_miejsc_sprzedanych_w_2_rzedzie > ilosc_miejsc_sprzedanych_w_1_rzedzie:
    print(f"Najwięcej miejsc sprzedaliśmy w 2 rzędzie. Było to: {ilosc_miejsc_sprzedanych_w_2_rzedzie} biletów")
else:
    print(f"Sprzedaliśmy po tyle samo biletów w obydwu rzędach. Było to: {ilosc_miejsc_sprzedanych_w_1_rzedzie} biletów")
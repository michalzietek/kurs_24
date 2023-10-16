lista_uczniow = ["Michal Zietkowski", "Jan Kowalski", "Adam Bak"]
lista_roznych_wartosci = ["Michal Zietkowski", 25, True, ["Jan Kowalski", "Adam Bak"]]
#print(lista_uczniow)
lista_uczniow[0] = "Mateusz Zietkowski"
#print(lista_uczniow)
#print(lista_roznych_wartosci)
#print(lista_roznych_wartosci[3])
lista_roznych_wartosci[3][0] = "Marcin Kowalski"
#print(lista_roznych_wartosci)

uczen_nr1 = lista_uczniow[0]
uczen_nr1 = "Jacek Bak"
lista_uczniow[0] = "Jacek Bak"
# print(lista_uczniow)
# print(uczen_nr1)

# for uczen in lista_uczniow:
#     print(uczen)
#
# for uczen in lista_uczniow:
#     if uczen == "Jan Kowalski":
#         print("Znalezlismy Jana Kowalskiego")

# print(lista_uczniow)
# for index, uczen in enumerate(lista_uczniow):
#     if uczen == "Jan Kowalski":
#         lista_uczniow[index] = "Maria Kowalska"
#
# print(lista_uczniow)
#
# imie = input("Podaj mi swoje imię: ")
# nazwisko = input("Podaj mi swoje nazwisko: ")
#
# lista_uczniow.append(f"{imie} {nazwisko}")
# print(lista_uczniow)
#
# lista_uczniow.remove(0)
# print(lista_uczniow)

# lista_uczniow.insert(1, "Jan Bednarek")
# print(lista_uczniow)
#
# print(lista_uczniow.index("Jan Bednarek"))
#
# for index, uczen in enumerate(lista_uczniow):
#     print(f"{index}: {uczen}")
#
#
# uczniowie_w_stringu = "Michal Zietkowski, Jan Bednarek, Maciej Dubij"
# lista_uczniow_ze_stringa = uczniowie_w_stringu.split(",")
# print(lista_uczniow_ze_stringa)
###########
#krotki
# plec = ("mezczyzna", "kobieta")
# lista_obecnosci = [(True, False), (True, False), (1, 0)]
# lista_obecnosci.append((2, 3))
# print(lista_obecnosci)
# plec_2 = "mezczyzna", "kobieta"
# plec_2 = "kobieta"
# plec_mezczyzny_z_tupli = plec[0]
# print(plec_mezczyzny_z_tupli)
# print(plec.index("kobieta"))
# plec_lista = list(plec)
# print(plec_lista)
# plec_tuple_z_listy = tuple(plec_lista)
# print(plec_tuple_z_listy)

#########
#zbiory

# lista_ocen = [1, 2, 3, 5, 1, 3]
# print(lista_ocen)
# zbior_z_listy = set(lista_ocen)
# print(zbior_z_listy)
# zbior_uczniow = {"Michal Zietkowski", "Jan Bednarek", "Jacek Gmoch"}
# for uczen in zbior_uczniow:
#     if uczen == "Michal Zietkowski":
#         znaleziony_uczen = uczen

# print(znaleziony_uczen)
# zbior_uczniow.add("Maciej Nowak")
# zbior_uczniow.remove("Jan Bednarek")
# print(zbior_uczniow)
###########################
## slowniki
#
# uzytkownik_slownik = {
#     "imie": "Michal",
#     "nazwisko": "Zietkowski",
#     "email": "michalzietkowski@gmail.com",
#     "wiek": 28
# }
# lista_uzytkownikow = [uzytkownik_slownik]
# imie_uzytkownika = uzytkownik_slownik["imie"]
# uzytkownik_slownik["plec"] = "mezczyzna"
# plec_uzytkownika = uzytkownik_slownik.get("plec", "kobieta")
# print(plec_uzytkownika)
# # print(uzytkownik_slownik["imie"])
# lista_ocen = [5, 4, 3, 5, 1]
# # lista_ocen[0] = 2
# # uzytkownik_slownik["imie"] = "Jacek"
# print(uzytkownik_slownik)
# for ocena in lista_ocen:
#     print(ocena)
#
# for informacja_o_uzytkowniku in uzytkownik_slownik:
#     print(informacja_o_uzytkowniku)
#
# for wartosc_informacji in uzytkownik_slownik.values():
#     print(wartosc_informacji)
#
# for klucz, wartosc in uzytkownik_slownik.items():
#     print(f"{klucz}: {wartosc}")

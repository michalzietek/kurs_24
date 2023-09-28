imie = "Michał" #zmienna typu tekstowego

# nowe_imie = "Mateusz"
# print(nowe_imie)
# typy liczbowe

moj_wiek = 18 #int
moje_wynagrodzenie = 3120.25

# print(type(moje_wynagrodzenie))
# print(moj_wiek + 2)
# print(moj_wiek-7)
# print(moj_wiek * 2)
# print(type(moj_wiek/2))
# print(moj_wiek ** 2)
# print(moj_wiek % 4)
# print(moj_wiek + moje_wynagrodzenie)

# typy boolean (prawda fałsz)
uzytkownik_ma_18_lat = True
uzytkownik_jest_na_emeryturze = False

#operacje logiczne
moj_wiek_jest_wiekszy_od_18_lat = moj_wiek > 18
moj_wiek_jest_wiekszy_rowny_18_lat = moj_wiek >= 18
moj_wiek_jest_rowny_18_lat = moj_wiek == 18
moj_wiek_jest_mniejszy_rownu_18_lat = moj_wiek <= 18
# print(moj_wiek_jest_wiekszy_od_18_lat)
#print(moj_wiek_jest_wiekszy_rowny_18_lat)

#operacja logiczna and i or

jestem_w_wieku_pracujacym = 18 < moj_wiek and moj_wiek < 65
print(jestem_w_wieku_pracujacym)

jestem_w_wieku_nie_pracujacym = moj_wiek <= 18 or moj_wiek > 65
print(jestem_w_wieku_nie_pracujacym)


#zmienne typu tekstowego
moje_imie = "Tomasz"

powiel_moje_imie = moje_imie * 2
print(powiel_moje_imie)

nowy_napis_witajcy_klientow_w_moim_sklepie = f'Witaj w moim sklepie {moje_imie}'
print(nowy_napis_witajcy_klientow_w_moim_sklepie)

moje_imie_i_nazwisko = moje_imie + " " + "Zietkowski"
print(moje_imie_i_nazwisko)

nowy_napis_witajcy_klientow_w_moim_sklepie_po_staremu = 'Witaj w moim sklepie {moje_imie}'.format(moje_imie=moje_imie_i_nazwisko)
print(nowy_napis_witajcy_klientow_w_moim_sklepie_po_staremu)

#zmienne typu null
imie_mojej_zony = None

#operacja wejscia
wiek_uzytkownika = input("Podaj mi swój wiek: ") #zawsze zmienna typu tekstowego
wiek_uzytkownika_jako_liczba = int(wiek_uzytkownika)
print(f"Wiek twojego użytkownika to: {wiek_uzytkownika}")
print(f"Osoba 2 razy starsza od użytkownika ma: {wiek_uzytkownika_jako_liczba*2} lat")


float(wiek_uzytkownika)
bool(wiek_uzytkownika)
str(wiek_uzytkownika)

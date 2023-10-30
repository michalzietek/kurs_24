liczba_elementow = int(input("Podaj mi ilość elementów: "))
suma_wszystkich_kilogramow = 0
waga_paczki = 0
ilosc_paczek = 1
suma_pustych_kiloramow = 0
paczka_z_najwieksza_iloscia_pustych_kg = 1
najwiecej_pustych_kilogramow = 0
for element in range(liczba_elementow):
    waga_elementu = float(input("Podaj mi wagę elementu: "))
    suma_wszystkich_kilogramow += waga_elementu
    if waga_elementu + waga_paczki < 20:
        waga_paczki += waga_elementu
    else:
        suma_pustych_kiloramow += (20 - waga_paczki)
        puste_kg_w_tej_paczce = 20 - waga_paczki
        if puste_kg_w_tej_paczce > najwiecej_pustych_kilogramow:
            paczka_z_najwieksza_iloscia_pustych_kg = ilosc_paczek
            najwiecej_pustych_kilogramow = puste_kg_w_tej_paczce
        ilosc_paczek += 1
        waga_paczki = waga_elementu
puste_kg_w_ostatniej_paczce = 20 - waga_paczki
suma_pustych_kiloramow += (20 - waga_paczki)
if puste_kg_w_ostatniej_paczce > najwiecej_pustych_kilogramow:
    paczka_z_najwieksza_iloscia_pustych_kg = ilosc_paczek
    najwiecej_pustych_kilogramow = puste_kg_w_ostatniej_paczce
print(f"Suma wszystkich kg wyslanych to: {suma_wszystkich_kilogramow}")
print(f"Ilosc paczek to: {ilosc_paczek}")
print(f"Liczba pustych kg w paczkach to: {suma_pustych_kiloramow}")
print(f"Najmniej kg było wysłanych w paczce {paczka_z_najwieksza_iloscia_pustych_kg}, było to: {najwiecej_pustych_kilogramow}")
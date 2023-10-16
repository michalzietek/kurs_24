import sys

uzytkownicy = [
    {
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "wiek": 28
    }
]

for uzytkownik in sys.argv[1:-2]:
    informacje_o_uzytkowniku = uzytkownik.split(",")
    print(informacje_o_uzytkowniku)
    uzytkownicy.append({
        "imie": informacje_o_uzytkowniku[0],
        "nazwisko": informacje_o_uzytkowniku[1],
        "wiek": int(informacje_o_uzytkowniku[2])
    })

print(uzytkownicy)

suma_wieku_uzytkownikow = 0
for uzytkownik in uzytkownicy[int(sys.argv[-2]): int(sys.argv[-1])]:
    wiek_uzytkownika = uzytkownik.get("wiek", 0)
    suma_wieku_uzytkownikow += wiek_uzytkownika

print(suma_wieku_uzytkownikow)
print(f"Średni wiek naszych użytkowników to: {round(suma_wieku_uzytkownikow/len(uzytkownicy), 2)}")

for uzytkownik in uzytkownicy:
    print(f"Użytkownik o imieniu: {uzytkownik.get('imie')}, nazwisku: {uzytkownik.get('nazwisko')} i wieku: {uzytkownik.get('wiek')}")

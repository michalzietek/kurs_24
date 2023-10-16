import sys

saldo = 10000
magazyn = [
    {
        "id": 1,
        "nazwa": "lodka",
        "ilosc": 5,
        "cena jednostkowa": 1000
    },
    {
        "id": 2,
        "nazwa": "aut",
        "ilosc": 4,
        "cena jednostkowa": 500
    }
]

historia = ["Utworzylem magazyn", "Zakupilem 1 lodke za 1000 zl", "Kupilem auto za 500 zl", "Sprzedalem 2 auta za 1000 zl"]
print(len(magazyn))
argumenty = sys.argv
for index, wartosc in enumerate(argumenty):
    if index == 1:
        operacja = wartosc

#skorzystac z instrukcji warunkowych

if operacja == "saldo":
    saldo += int(sys.argv[2])
    historia.append(sys.argv[3])
elif operacja == "przegląd":
    print(historia[0:3])
print(saldo)
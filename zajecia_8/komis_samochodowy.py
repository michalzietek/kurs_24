counter = 1

class Samochod:
    def __init__(self, marka, model, przebieg, cena, licznik):
        self.id = licznik
        self.marka = marka
        self.model = model
        self.przebieg = przebieg
        self.cena = cena
        self.oferta_aktualna = True

    def __repr__(self):
        return f"Samochod {self.marka + self.model} o id {self.id} i cenie: {self.cena}"

    def obniz_cene_auta(self, nowa_cena):
        self.cena = nowa_cena
komis_samochodowy = []

print("Witaj w programie obslugi komisu samochodowego. Co chcesz zrobić aktualnie?")
koniec_programu = False
while not koniec_programu:
    wybor_opcji = input("Podaj co chcesz zrobic ")
    if wybor_opcji == "kupno":
        marka_auta = input("Podaj marke ")
        model_auta = input("Podaj model ")
        przebieg_auta = input("Podaj przebieg ")
        cena_auta = input("Podaj cene ")
        komis_samochodowy.append(Samochod(marka=marka_auta, model=model_auta, przebieg=przebieg_auta, cena=cena_auta, licznik=counter))
        counter += 1
    elif wybor_opcji == "koniec":
        koniec_programu = True
    elif wybor_opcji == "cena":
        print(komis_samochodowy)
        id_pojazdu = input("Podaj mi pojazd, w którym chcesz obnizyc cene")
        wybrany_pojazd = None
        for pojazd in komis_samochodowy:
            if pojazd.id == int(id_pojazdu):
                wybrany_pojazd = pojazd
        nowa_cena = input("Podaj nową cenę auta")
        wybrany_pojazd.obniz_cene_auta(nowa_cena)

print(komis_samochodowy)

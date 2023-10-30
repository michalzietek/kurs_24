class PrzepisNaMakowiec:
    def __init__(self, maka, jajka, mak):
        self.ilosc_maki = maka
        self.ilosc_maku = mak
        self.ilosc_jajek = jajka

    def ubij_jajka(self):
        print(f"Ubilismy jajka w ilosci {self.ilosc_jajek}")
        return 20

    def upiecz_ciast(self):
        print(f"Upieklismy ciasto z {self.ilosc_maku} maku i {self.ilosc_maki} mąki")


# makowiec = PrzepisNaMakowiec(maka=100, jajka=2, mak=50)
#
# makowiec_2 = PrzepisNaMakowiec(maka=500, jajka=4, mak=200)
#
# dowolna_liczba = makowiec.ubij_jajka()
#
# makowiec_2.ubij_jajka()
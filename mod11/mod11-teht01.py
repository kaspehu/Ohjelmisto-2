class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print("Julkaisu")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivut):
        self.kirjailija = kirjailija
        self.sivut = sivut
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, sivumäärä: {self.sivut}, kirjailija: {self.kirjailija}")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, päätoimittaja: {self.päätoimittaja}")


kirja = Kirja("Hytti no:6", "Rosa Liksom", "200")
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisut = []
julkaisut.append(kirja)
julkaisut.append(lehti)

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()
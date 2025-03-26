class Julkaisu:
    def __init__(self, tyyppi, julkaisun_nimi):
        self.tyyppi = tyyppi
        self.julkaisun_nimi = julkaisun_nimi

    def tulosta_tiedot(self):
        print(f'{self.tyyppi}: {self.julkaisun_nimi}')



class Kirja(Julkaisu):
    def __init__(self, julkaisun_nimi, kirjoittaja, sivumäärä):
        super().__init__("Kirja", julkaisun_nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'  - Kirjoittaja: {self.kirjoittaja}')
        print(f'  - Sivumäärä: {self.sivumäärä}')



class Lehti(Julkaisu):
    def __init__(self, julkaisun_nimi, päätoimittaja):
        super().__init__("Lehti", julkaisun_nimi)
        self.päätoimittaja = päätoimittaja
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'  - Päätoimittaja: {self.päätoimittaja}')



julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()



class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        if self.nykyinen_nopeus + nopeuden_muutos < 0:# jos nopeus menisi alle 0, muutetaan nyk.nopeus -> 0
            self.nykyinen_nopeus = 0 
        elif self.nykyinen_nopeus + nopeuden_muutos > self.huippunopeus:# jos nopeus menisi yli huippunopeuden, muutetaan nyk.nopeus -> huippunopeus
            self.nykyinen_nopeus = self.huippunopeus
        else:# muuten lisätään nopeuden muutos nykyiseen nopeuteen
            self.nykyinen_nopeus += nopeuden_muutos

    def kulje(self, tunnit):
        self.kuljettu_matka = self.nykyinen_nopeus * tunnit


def pääohjelma():
    auto_lista = []
    auto_lista.append(Auto("ABC-123", 142))

    auto_lista[0].kiihdytä(60)
    print(f'Auton nopeus: {auto_lista[0].nykyinen_nopeus} km/h')

    print(f'Kuljettu matka alussa: {auto_lista[0].kuljettu_matka} km')

    print(f'Autolla matkustetaan: 1,5 h')
    auto_lista[0].kulje(1.5)

    print(f'Kuljettu matka lopussa: {auto_lista[0].kuljettu_matka} km')



pääohjelma()
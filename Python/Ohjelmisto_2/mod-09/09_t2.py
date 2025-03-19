class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus=0, kuljettu_matka=0):
        Auto.rekisteritunnus = rekisteritunnus
        Auto.huippunopeus = huippunopeus
        Auto.nykyinen_nopeus = nykyinen_nopeus
        Auto.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        if self.nykyinen_nopeus + nopeuden_muutos < 0:# jos nopeus menisi alle 0, muutetaan nyk.nopeus -> 0
            self.nykyinen_nopeus = 0 
        elif self.nykyinen_nopeus + nopeuden_muutos > self.huippunopeus:# jos nopeus menisi yli huippunopeuden, muutetaan nyk.nopeus -> huippunopeus
            self.nykyinen_nopeus = self.huippunopeus
        else:# muuten lisätään nopeuden muutos nykyiseen nopeuteen
            self.nykyinen_nopeus += nopeuden_muutos


def pääohjelma():
    auto_lista = []
    auto_lista.append(Auto("ABC-123", 142))

    auto_lista[0].kiihdytä(30)
    auto_lista[0].kiihdytä(70)
    auto_lista[0].kiihdytä(50)
    print(auto_lista[0].nykyinen_nopeus)
    auto_lista[0].kiihdytä(-200)
    print(auto_lista[0].nykyinen_nopeus)



pääohjelma()
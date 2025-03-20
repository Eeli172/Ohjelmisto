import random
from prettytable import PrettyTable


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if self.nykyinen_nopeus + nopeuden_muutos < 0:# jos nopeus menisi alle 0, muutetaan nyk.nopeus -> 0
            self.nykyinen_nopeus = 0 
        elif self.nykyinen_nopeus + nopeuden_muutos > self.huippunopeus:# jos nopeus menisi yli huippunopeuden, muutetaan nyk.nopeus -> huippunopeus
            self.nykyinen_nopeus = self.huippunopeus
        else:# muuten lisätään nopeuden muutos nykyiseen nopeuteen
            self.nykyinen_nopeus += nopeuden_muutos

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit


class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, auto_lista):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.auto_lista = auto_lista
        self.kilpailu_ohi_bool = False
        
    
    def tunti_kuluu(self):
        for auto in self.auto_lista:
            auto.kiihdytä(int(random.randint(-10, 15)))
            auto.kulje(1)

    def tulosta_tilanne(self):
        tulostus = PrettyTable()
        tulostus.field_names = ["Rekisteritunnus", "Huippunopeus km/h", "Kuljettu matka km"]

        self.auto_lista.sort(key = lambda a: a.kuljettu_matka, reverse=True)
        
        for auto in self.auto_lista:
            tulostus.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.kuljettu_matka])
        print(tulostus)

    def kilpailu_ohi(self):
        for auto in self.auto_lista:
            if auto.kuljettu_matka >= self.pituus_km:# jos auto on kulkenut kilpailun pituuden verran, voittaja julistetaan ja looppi suljetaan
                print(f'\n{auto.rekisteritunnus} voitti kilpailun!'.upper())
                return True
            else: return False


### Pääohjelma ###

# luodaan autolista
auto_lista = []
for i in range(1,11):
    auto_lista.append(Auto(f"ABC-{i}", int(random.randint(100, 200))))

# luodaan romuralli
romuralli = Kilpailu("Suuri romuralli", 8000, auto_lista)

# ralli alkaa
kierros = 0
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    kierros += 1
    if kierros % 10 == 0:
        romuralli.tulosta_tilanne()

romuralli.tulosta_tilanne()
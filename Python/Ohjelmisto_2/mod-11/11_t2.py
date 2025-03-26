# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. 
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

import random


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



class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kWh = akkukapasiteetti_kWh


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko_litra):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko_litra = tankin_koko_litra


autolista = []
autolista.append(Sähköauto('ABC-15', 180, 52.5))
autolista.append(Polttomoottoriauto('ACD-123', 165, 32.3))

for auto in autolista:
    auto.kiihdytä(random.randint(10, auto.huippunopeus))
    auto.kulje(3)
    print(f'Matkamittarilukema: {auto.kuljettu_matka} km')    

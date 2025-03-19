# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. 
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#       - Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
#         Tämä tehdään kutsumalla kiihdytä-metodia.
#       - Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# 
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

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
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit


def pääohjelma():
    auto_lista = []

    for i in range(1,11):
        auto_lista.append(Auto(f"ABC-{i}", int(random.randint(100, 200))))

    kilpailu_käynnissä = True
    while kilpailu_käynnissä:

        for auto in auto_lista:# muutetaan vuorollaan kunkin auton nopeus ja kuljettu matka 
            auto.kiihdytä(int(random.randint(-10, 15)))
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:# jos auton kulkema matka on 10000 km tai yli, voittaja julistetaan ja looppi suljetaan
                print(f'{auto.rekisteritunnus} voitti kilpailun!')
                kilpailu_käynnissä = False


pääohjelma()

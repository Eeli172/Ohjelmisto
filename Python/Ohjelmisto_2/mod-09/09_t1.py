class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = kuljettu_matka

def pääohjelma():
    auto_lista = []

    auto_lista.append(Auto("ABC-123", 142))

    print(f"Auton, jonka rekisteritunnus on {auto_lista[0].rekisteritunnus}, huippunopeus on {auto_lista[0].huippunopeus} km/h")

pääohjelma()
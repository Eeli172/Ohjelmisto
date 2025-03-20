class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

def pääohjelma():
    auto_lista = []

    auto_lista.append(Auto("ABC-123", 142))

    print(f"Auton, jonka rekisteritunnus on {auto_lista[0].rekisteritunnus}, huippunopeus on {auto_lista[0].huippunopeus} km/h")

pääohjelma()
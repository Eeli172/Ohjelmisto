# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def noppa():
    x = int(random.randint(1,6))
    return x

tulos = 0

while tulos != 6:
    tulos = noppa()
    print(f"Nopasta saatu silmäluku: {tulos}")
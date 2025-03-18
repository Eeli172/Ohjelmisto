import random

def noppa():
    x = int(random.randint(1,6))
    return x

tulos = 0

while tulos != 6:
    tulos = noppa()
    print(f"Nopasta saatu silmäluku: {tulos}")
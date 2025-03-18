import random
tahko = int(input("Anna nopan tahkojen määrä: "))

def noppa():
    x = int(random.randint(1,tahko))
    return x

tulos = 0

while tulos != tahko:
    tulos = noppa()
    print(f"Nopasta saatu silmäluku: {tulos}")
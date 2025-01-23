import random

arpakuutio_lkm = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(arpakuutio_lkm):
    summa += random.randint(1,6)

print(f"{arpakuutio_lkm} kpl noppia heitetty, saatujen silmälukujen summa: {summa}")
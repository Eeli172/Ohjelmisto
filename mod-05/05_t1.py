import random

arpakuutio_lkm = int(input("Anna arpakuutioiden lukumäärä: "))
arpakuutiot = []

for i in range(arpakuutio_lkm):
    arpakuutiot.append(random.randint(1,6))

print(f"{len(arpakuutiot)} kpl noppia heitetty, saatujen silmälukujen summa: {sum(arpakuutiot)}")
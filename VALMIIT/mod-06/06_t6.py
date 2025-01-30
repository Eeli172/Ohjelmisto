import math

def pizzaPrice(diam_cm:float,price:float):
    radius_m = diam_cm/100/2
    sqm = math.pi*radius_m**2
    price_sqm = price / sqm
    return price_sqm

diam1 = float(input("Anna pizzan 1 halkaisija senttimetreinä: "))
pric1 = float(input("Anna pizzan 1 hinta euroina: "))
diam2 = float(input("Anna pizzan 2 halkaisija senttimetreinä: "))
pric2 = float(input("Anna pizzan 2 hinta euroina: "))

pric_sqm1 = pizzaPrice(diam1, pric1)
pric_sqm2 = pizzaPrice(diam2, pric2)

if pric_sqm1 < pric_sqm2:
    print(f"Pizzalla 1 on halvempi suhteellinen hinta. Pizza maksoi {pric_sqm1} € / neliömetri. ")
elif pric_sqm2 < pric_sqm1:
    print(f"Pizzalla 2 on halvempi suhteellinen hinta. Pizza maksoi {pric_sqm1} € / neliömetri. ")
else:
    print(f"Pizzojen hinnat ovat samat neliömetriä kohden {pric_sqm1}")

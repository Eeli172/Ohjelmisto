import math

kanta_float = float(input("Kanta (M3): "))
korkeus_float = float(input("Korkeus (M3): "))

pinta_ala_float = kanta_float * korkeus_float
piiri_float = 2 * (kanta_float + korkeus_float)

print(f"Pinta-ala on {pinta_ala_float} M3 ja piiri on {piiri_float} M3")


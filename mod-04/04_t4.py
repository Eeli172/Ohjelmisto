import random

randomi = random.randint(1,10)
arvaus = 0

while randomi != arvaus:
    arvaus = int(input("\nArvaa tietokoneen arpoma kokonaisluku väliltä 1 ja 10: "))
    if randomi == arvaus:
        print(f"\n\nArvasit oikein, tietokoneen arpoma luku oli {randomi}\n\n")
    else:
        print("\nVäärä arvaus, yritä uudelleen. ")
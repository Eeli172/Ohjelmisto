import random

randomi = random.randint(1,10)

while 1:
    arvaus = int(input("\nArvaa tietokoneen arpoma kokonaisluku väliltä 1 ja 10: "))
    if randomi == arvaus:
        print(f"\n\nArvasit oikein, tietokoneen arpoma luku oli {randomi}\n\n")
        break
    print("\nVäärä arvaus, yritä uudelleen. ")
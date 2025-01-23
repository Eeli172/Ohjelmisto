import math

pienin = math.inf
suurin = -math.inf

syöte_str = str(input("\nAnna ensimmäinen luku: "))

while syöte_str != "":

    syöte = float(syöte_str)

    if pienin > syöte:
        pienin = syöte

    if suurin < syöte:
        suurin = syöte

    syöte_str = str(input("\nAnna uusi luku"))

if pienin != math.inf:
    print(f"\nPienin syöttämäsi luku on {pienin} ja suurin syöttämäsi luku on {suurin}\n")
else: 
    print("\nEt syöttänyt yhtään lukua.\n")
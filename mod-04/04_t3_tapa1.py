pienin = ""
suurin = ""
print("\nSyötä lukuja, ohjelma kerää näistä suurimman ja pienimmän. \nPäätä ohjelma syöttämällä tyhjä merkkijono. \nLopussa ohjelma tulostaa syöttämistäsi luvuista pienimmän ja suurimman.\n")

while 1:
    x = str(input("Syötä luku: "))
    if x == "":
        print("\nSyötit tyhjän merkkijonon, ohjelma päättyy.")
        break
    elif pienin == "":
        pienin = float(x)
        suurin = float(x)
    elif float(pienin) > float(x):
        pienin = float(x)
    elif float(suurin) < float(x):
        suurin = float(x)

if type(pienin) == float:
    print(f"\nPienin syöttämäsi luku on {pienin} ja suurin syöttämäsi luku on {suurin}\n")
else: 
    print("Et syöttänyt yhtään lukua.")
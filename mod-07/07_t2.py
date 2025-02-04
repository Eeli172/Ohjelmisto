nimet = set()
nimi = str(input("Syötä nimi: "))

while nimi != "":

    if nimi in nimet:
        print("Aiemmin syötetty nimi. ")

    else:
        print("Uusi nimi. ")

    nimet.add(nimi)
    nimi = str(input("Syötä nimi: "))

for n in nimet:
    print(n)
lista = []
syöte_str = str(input("Syötä ensimmäinen luku: "))

while syöte_str != "":
    syöte_float = float(syöte_str)
    lista.append(syöte_float)
    syöte_str = str(input("Syötä uusi luku: "))

lista.sort(reverse=True)

if len(lista) >= 5:
    print("Viisi suurinta syöttämääsi numeroa järjestettynä suurimmasta pienimpään")

    for i in range(0,5):
        print(lista[i])
else:
    print(f"Syötit {len(lista)} kpl numeroita, tässä numerot järjestettynä suurimmasta pienimpään:")
    for i in range(0,len(lista)):
        print(lista[i])

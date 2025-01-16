sukupuoli = str(input("Anna biologinen sukupuolesi (n/m): "))
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "n":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on liian pieni.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on liian suuri.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "m": 
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on liian pieni.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on liian suuri.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
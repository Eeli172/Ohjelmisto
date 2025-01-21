cm = float()

print("Anna senttimetrit tuumiksi muutettavaksi. Päätä ohjelma syöttämällä negatiivinen luku.")


while cm >= 0:
    cm = float(input("Anna senttimetrit: "))
    print(f"Antamasi senttimetrit ovat {cm*2.54:.2f} tuumaa")


print("Syötit negatiivisen luvun, ohjelma suljetaan.")
luku1_int = int(input("Anna luku: "))
luku2_int = int(input("Anna toinen luku: "))
luku3_int = int(input("Anna kolmas luku: "))

summa_int = int(luku1_int + luku2_int + luku3_int)
tulo_int  = int(luku1_int * luku2_int * luku3_int)
keskiarvo_float = float((luku1_int + luku2_int + luku3_int) / 3)
keskiarvo_round = round(keskiarvo_float, 2)

print(f"Antamiesi lukujen summa on {summa_int}, tulo on {tulo_int} ja keskiarvo on {keskiarvo_round}")
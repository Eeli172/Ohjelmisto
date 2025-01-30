gallona = float(input("Anna gallonat, päätä ohjelma syöttämällä negatiivinen luku: "))

def gal_to_l(gal):
    l = gal * 3.785
    return l

while gallona >= 0:
    print(f"{gallona} gallonaa on {gal_to_l(gallona)} litraa")
    gallona = float(input("Anna gallonat, päätä ohjelma syöttämällä negatiivinen luku: "))


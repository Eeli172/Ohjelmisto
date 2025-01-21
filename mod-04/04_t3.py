list_of_numbers = []

# tarkistaa, onko kyseessä integer, palauttaa boolean -arvon
def is_integer(variable): 
    try: 
        int(variable) 
        return True 
    except ValueError: 
        return False 
    
# tarkistaa, onko kyseessä float, palauttaa boolean -arvon
def is_float(variable): 
    try: 
        float(variable) 
        return True 
    except ValueError: 
        return False 

while True:
    inp = input("Anna luku: ")

# käyttäjän syöttämä tyhjä merkkijono katkaisee loopin
    if inp == "":
        print("Syötit tyhjän merkkijonon, ohjelma sulkeutuu.")
        break

# integer sekä float -arvoiksi hyväksytyt syötteet lisätään listalle
    elif is_integer(inp):
        inp = int(inp)
        list_of_numbers.append(inp)
    elif is_float(inp):
        inp = float(inp)
        list_of_numbers.append(inp)

# muun muotoiset syötteet palauttavat käyttäjälle virheilmoituksen
    else:
        print("Syötit virheellisen arvon, yritä uudelleen. Tyhjä merkkijono päättää ohjelman. ")


try: 
    print(f"Pienin antamasi numero: {min(list_of_numbers)}")
    print(f"Suurin antamasi numero: {max(list_of_numbers)}")
except ValueError:
    print("Et syöttänyt yhtään lukua.")
list_of_numbers = []
def to_integer(s): 
    try: 
        int(s) 
        return True 
    except ValueError: 
        return False 
def to_float(s): 
    try: 
        float(s) 
        return True 
    except ValueError: 
        return False 

while True:
    inp = input("Anna luku: ")
    if inp == "":
        print("Syötit tyhjän merkkijonon, ohjelma sulkeutuu.")
        break
    elif to_integer(inp):
        inp = int(inp)
        list_of_numbers.append(inp)
    elif to_float(inp):
        inp = float(inp)
        list_of_numbers.append(inp)

print(list_of_numbers)
print(f"Pienin antamasi numero: {min(list_of_numbers)}")
print(f"Suurin antamasi numero: {max(list_of_numbers)}")
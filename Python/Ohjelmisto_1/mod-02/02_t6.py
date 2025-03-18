import random

loop=0
kolme=str()
neljä=str(random.randint(1,6))


while loop < 3:
    kolme += str(random.randint(0,9))
    neljä += str(random.randint(1,6))
    loop += 1


# fiksumpi tapa: 
# kolme = "".join(str(random.randint(0,9)) for i in range(3))
# neljä = "".join(str(random.randint(1,6)) for i in range(4))


print(f"kolmenumeroinen koodi: {kolme}")
print(f"nelinumeroinen koodi: {neljä}")
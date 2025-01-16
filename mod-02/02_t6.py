import random

loop=0
kolme=str()
neljä=str(random.randint(1,6))


while loop < 3:
    kolme += str(random.randint(0,9))
    neljä += str(random.randint(1,6))
    loop += 1

print(f"kolmenumeroinen koodi: {kolme}")
print(f"nelinumeroinen koodi: {neljä}")
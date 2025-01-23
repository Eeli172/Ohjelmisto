import random

N = int(1000000)
n = int()

loop = 0

while N != loop:
    X = random.uniform(-1,1)
    Y = random.uniform(-1,1)
    if X ** 2 + Y ** 2 < 1:
        n +=1

    loop += 1

print(f"Piin laskettu likiarvo on: {4*n/N:.4f}")

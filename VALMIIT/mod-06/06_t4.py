def listsum(lista:list):
    x = 0
    for num in lista:
        x += num
    return x

numerot = [8,3,45,47,24,37,54,2,5,8,6,45,45,2,55,65,18,241,67]

print(f"listan numeroiden summa: {listsum(numerot)}")
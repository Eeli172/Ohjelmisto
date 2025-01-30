def rm_odd(lista:list[int]):
    even = []
    for num in lista:
        if num % 2 == 0:
            even.append(num)
    return even

numerot = [8,3,45,47,24,37,54,2,6,-2,-6,-5,6,5,2,1,0,5,8,6,45,45,2,55,65,15,-2,1,-23,-8,241,67]
print(numerot)
print(rm_odd(numerot))
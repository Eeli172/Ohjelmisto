koko = (int(input("Anna luku: ")) // 2)
x = int(1)
st = "*"
for z in range(koko):
    print(f"{st*x:>(koko)s}")
    x += 2
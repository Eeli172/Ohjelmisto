# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
pienin = float()
suurin = float()
print(pienin)

while 1:
    x = input("Syötä luku: ")
    if pienin == float():
        pienin = x
        suurin = x
        print(type(pienin))

print(x)


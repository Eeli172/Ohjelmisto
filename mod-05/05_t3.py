kokonaisluku = int(input("Syötä kokonaisluku: "))
alkuluku = True

if kokonaisluku > 0:
    for i in range(2, kokonaisluku):
        if kokonaisluku % i == 0:
            alkuluku = False
else:
    for i in range(2, -kokonaisluku):
        if kokonaisluku % i == 0:
            alkuluku = False

if alkuluku:
    print("Syöttämäsi luku on alkuluku. ")
else:
    print("Syöttämäsi luku ei ole alkuluku. ")

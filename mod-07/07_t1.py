vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kk = int(input("Anna kuukauden numero: "))

if 3 <= kk <= 5:
    print(vuodenajat[0])
elif 6 <= kk <= 8:
    print(vuodenajat[1])
elif 9 <= kk <= 11:
    print(vuodenajat[2])
elif 1 <= kk <= 12:
    print(vuodenajat[3])

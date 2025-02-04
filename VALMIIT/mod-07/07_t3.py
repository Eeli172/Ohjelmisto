db = {}
ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))
while ip != 3:
    if ip == 1:
        icao = str(input("Syötä lentoaseman ICAO-koodi: "))
        nimi = str(input("Syötä lentoaseman nimi: "))
        db[icao] = nimi
    elif ip == 2:
        haku = str(input("Syötä haettavan lentoaseman ICAO-koodi: "))
        print(db[haku])
    else:
        print("Annoit virheellisen syötteen, anna jokin seuraavista numeroista [1, 2, 3]")
    ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))

print("Ohjelma sulkeutuu. ")
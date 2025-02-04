db = {}
ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))

while ip != 3:
# Jos käyttäjän syöte on 1 == hän haluaa syöttää uuden lentoaseman, hän pääsee syöttämään nuo, jonka jälkeen tiedot lisätään sanakirjaan
    if ip == 1:
        icao = str(input("Syötä lentoaseman ICAO-koodi: "))
        nimi = str(input("Syötä lentoaseman nimi: "))
        db[icao] = nimi
# Jos käyttäjän syöte on 2 == hän haluaa hakea sanakirjasta, niin hän pääsee hakemaan
    elif ip == 2:
        haku = str(input("Syötä haettavan lentoaseman ICAO-koodi: "))
        print(db[haku])
# Jos käyttäjä syöttää muuta, kun 1, 2, tai 3 niin hän saa palautetta virheellisestä syötteestä
    else:
        print("Annoit virheellisen syötteen, anna jokin seuraavista numeroista [1, 2, 3]")
    
    ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))

print("Ohjelma sulkeutuu. ")
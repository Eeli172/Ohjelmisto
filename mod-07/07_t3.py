# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, 
# kunnes hän haluaa lopettaa. 
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. 
# Löydät koodeja helposti selaimen avulla.)
db = set()
ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))
while ip != 3:
    if ip == 1:
        icao = str(input("Syötä lentoaseman ICAO-koodi: "))
        nimi = str(input("Syötä lentoaseman nimi: "))
        db.add((icao, nimi))
    elif ip == 2:
        haku = str(input("Syötä haettavan lentoaseman ICAO-koodi: "))
        for i in db:
            if i[0] == haku:
                print(i[1])
    else:
        print("Annoit virheellisen syötteen, anna jokin seuraavista numeroista [1, 2, 3]")
    ip = int(input("Haluatko: syöttää uuden lentoaseman [1], hakea jo syötetyn lentoaseman tiedot [2], vai lopettaa [3]: "))

print("Ohjelma sulkeutuu. ")
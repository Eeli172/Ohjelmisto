import mysql.connector

def airport_types(country):
    sql = f"select type, iso_country from airport where iso_country = '{country}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    # käydään rivit läpi, lisätään sanakirjaan kukin tyyppi ja lasketaan kuinka monta kertaa tyyppi ilmaantuu
    numerot = {}
    for rivi in tulos:
        if rivi[0] in numerot:
            numerot[rivi[0]] += 1
        else:
            numerot[rivi[0]] = 1
    # tulostetaan sanakirjasta kukin tyyppi ja sitä vastaava lukumäärä
    for i in numerot:
        print(f'{i}: {numerot[i]}')

    
yhteys = mysql.connector.connect(
    collation = "utf8mb4_general_ci",
    host = '127.0.0.1',
    port = 3306,
    database = "flight_game",
    user = "python",
    password = "koulu123",
    autocommit = True
)

inp = str(input("maakoodi: "))
airport_types(inp)

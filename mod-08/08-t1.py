import mysql.connector

def lentoasema_haku(icao):
    sql = f"select name, municipality, ident from airport where ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if kursori.rowcount > 0:
        print(f"ICAO-koodi: {tulos[2]}\nLentoaseman nimi: {tulos[0]}\nLentoaseman sijainti: {tulos[1]}")
    else:
        print(f"Haullasi '{icao}' ei löytynyt yhtään lentoasemaa. ")

yhteys = mysql.connector.connect(
    collation = "utf8mb4_general_ci",
    host = '127.0.0.1',
    port = 3306,
    database = "flight_game",
    user = "python",
    password = "koulu123",
    autocommit = True
)

haku = str(input("Syötä lentoaseman ICAO-koodi: "))
lentoasema_haku(haku)


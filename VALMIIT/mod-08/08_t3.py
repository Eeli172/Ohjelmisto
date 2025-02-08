import mysql.connector
from geopy import distance


def icao_koordinaatti(icao):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos 

yhteys = mysql.connector.connect(
    collation = "utf8mb4_general_ci",
    host = '127.0.0.1',
    port = 3306,
    database = "flight_game",
    user = "python",
    password = "koulu123",
    autocommit = True
)

koordinaatit = []
for i in range(2):
    icao_str = str(input(f"Anna {i+1}. ICAO-koodi: "))
    koordinaatit.append(icao_koordinaatti(icao_str))

print(f"Etäisyys lentoasemien välillä on: {distance.distance((koordinaatit[0][0],koordinaatit[0][1]),(koordinaatit[1][0],koordinaatit[1][1]))}")

    
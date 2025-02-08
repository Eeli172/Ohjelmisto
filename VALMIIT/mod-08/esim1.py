import mysql.connector

def lemmikin_omistaja(lemmikin_nimi):
    sql = f"SELECT etunimi,sukunimi FROM ankkalinnalainen,omistaa,lemmikki where omistaa.lemmikki_id = lemmikki.id AND omistaa.ankkalinnalainen_id = ankkalinnalainen.id AND lemmikki.nimi = '{lemmikin_nimi}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"Lemmikin nimeltä {input} omistaa: ")
        for rivi in tulos:
            print(f"{rivi[0]} {rivi[1]}")
    else:
        print("Hakemaasi lemmikkiä ei löydy Ankkalinnasta.")
# Pääohjelma
yhteys = mysql.connector.connect(
    collation = "utf8mb4_general_ci",
    host = '127.0.0.1',
    port = 3306,
    database = "ankkalinna",
    user = "python",
    password = "koulu123",
    autocommit = True
)

input = str(input("Syötä Ankkalinnan lemmikin nimi: "))
lemmikin_omistaja(input)
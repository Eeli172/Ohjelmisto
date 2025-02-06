# Huom! Joillain käyttäjillä on ilmennyt yllättäviä haasteita uusimman MySQL-ajuriversion 8.0.30 kanssa. Jos törmäät virheilmoitukseen mysql.connector.errors.ProgrammingError: Character set 'utf8' unsupported, vaihda toiseksi uusimpaan ajuriversioon 8.0.29: Valitse PyCharmissa View/Tool Windows/Python Packages. Etsi hakutoiminnolla pakkaus mysql-connector-python. Poista version 8.0.30 asennus painamalla oikeassa laidassa olevaa kolmea pistettä ja valitsemalla Delete. Vaihda ajuriversioksi 8.0.29 Latest-valinnan tilalle ja asenna napsauttamalla Install.

# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
import mysql.connector


def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on: {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
    return


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    # Huom: käyttäjän root salasana EI saa olla root!!!
    user='root',
    password='root',
    autocommit=True
    )

icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)
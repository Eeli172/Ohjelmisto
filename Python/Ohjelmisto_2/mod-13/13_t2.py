from json import dumps
from flask import Flask, Response
import mysql.connector


yhteys = mysql.connector.connect(
    collation = "utf8mb4_general_ci",
    host = '127.0.0.1',
    port = 3306,
    database = "flight_game",
    user = "python",
    password = "koulu123",
    autocommit = True
)


app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{ICAO}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    json_tulos = dumps(tulos)
    
    return Response(response=json_tulos, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
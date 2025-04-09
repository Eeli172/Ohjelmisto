from flask import Flask, Response
from json import dumps

app = Flask(__name__)
@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        summa = float(luku1) + float(luku2)
    
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "kuvaus": 'Virheellinen yhteenlaskettava.'
        }

    json_vastaus = dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def sivua_ei_löydy(virhe):
        vastaus = {
            "status": virhe.code,
            "kuvaus": virhe.description
        }

        json_vastaus = dumps(vastaus)
        return Response(response=json_vastaus, status=virhe.code, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

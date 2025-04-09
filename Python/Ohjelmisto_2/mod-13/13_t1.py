from json import dumps
from flask import Flask, Response

app = Flask(__name__)
@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    numero = int(numero)
    alkuluku = True
    for i in range(2, numero):
        if numero % i == 0:
            alkuluku = False

    luku = {
        "Number": numero,
        "isPrime": alkuluku
    }

    json_luku = dumps(luku)
    return Response(response=json_luku, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

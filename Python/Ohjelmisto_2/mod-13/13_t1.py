from flask import Flask
from sympy import isprime

app = Flask(__name__)
@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    numero = int(numero)
    luku = {
        "Number": numero,
        "isPrime": isprime(numero)
    }
    return str(luku)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

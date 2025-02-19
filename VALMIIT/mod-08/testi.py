from sympy import *

a = symbols("a")
b = symbols("b")
c = symbols("c")
x = symbols("x")
y = symbols("y")
nimittäjä = input("Syötä nimittäjän arvo: ")
nimittäjä = sympify(nimittäjä)
osoittaja = input("Syötä osoittajan arvo: ")
osoittaja = sympify(osoittaja)

print(f"Tulos: {factor((nimittäjä)/(osoittaja))}")
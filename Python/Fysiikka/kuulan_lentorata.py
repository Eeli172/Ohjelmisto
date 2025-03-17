from math import sin, cos, radians
import matplotlib.pyplot as plt

g = 9.81 # painovoiman kiihtyvyys (m/s^2)
dt = 0.01 # aikavälin pituus (s)

x0 = 0.0
y0 = 1.8 # lähtökorkeus (m)
v0 = 13.0 # lähtönopeuden itseisarvo (m/s)
kulma = radians(35) # lähtökulma (suluissa asteina)

xlist = [x0] # lista, joka sisältää aluksi yhden alkion (lähtöarvo)
ylist = [y0]

vx = v0*cos(kulma) # HUOM: tämä on pelkkä muuttuja, ei lista
vylist = [v0*sin(kulma)]

while (ylist[-1] > 0):
    vylist.append(vylist[-1]-g*dt)
    xlist.append(xlist[-1]+vx*dt)
    vky = (vylist[-1]+vylist[-2])/2
    ylist.append(ylist[-1]+vky*dt)


plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xlist,ylist)
plt.show()

print(f'Pituus = {xlist[-1]:.1f} m.')
print(f'Lakikorkeus = {max(ylist):.2f} m.')
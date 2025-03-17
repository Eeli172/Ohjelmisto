import csv
import matplotlib.pyplot as plt


with open('hissidata.csv', mode = 'r') as hissidata:
    data = csv.reader(hissidata)

    # Kiihtyvyyden ja ajan erottelu omiin listoihin
    time = [0]
    acc = [0]
    for row in data:
        try:
            time.append(float(row[0]))
            acc.append(float(row[1]))
        except ValueError:
            pass
    
    # Kiihtyvyyden määrittely
    vel = [0]
    for i in range(len(acc)-1):
        ak = (acc[i]+acc[i+1])/2 # keskimääräinen kiihtyvyys
        dt = time[i+1]-time[i] # aikavälin pituus
        vel.append(vel[-1] + ak*dt)

    # Siirtymän määrittely
    x = [0]
    for i in range(len(vel)-1):
        vk = (vel[i]+vel[i+1])/2 # keskimääräinen nopeus
        dt = time[i+1]-time[i]
        x.append(x[-1] + vk*dt)

    inp = int(input("    1 - Kiihtyvyys-graafi\n    2 - Nopeus-graafi\n    3 - Siirtymä-graafi\n    0 - Sulje ohjelma\n\nValitse edellisistä: "))
    while inp != 0:
        if inp == 1: # Kiihtyvyys-graafi
            plt.xlabel('t (s)')
            plt.ylabel('a (m/s$^{2}$)')
            plt.plot(time,acc)
            plt.show()
    
        elif inp == 2: # Nopeus-graafi
            plt.xlabel('t (s)')
            plt.ylabel('v (m/s)')
            plt.plot(time,vel)
            plt.show()
        
        elif inp == 3: # Siirtymä-graafi 
            plt.xlabel('t (s)')
            plt.ylabel('x (m)')
            plt.plot(time,x)
            plt.show()

        else:
            print("Syötit määrittämättömän arvon, yritä uudelleen")
        inp = int(input("    1 - Kiihtyvyys-graafi\n    2 - Nopeus-graafi\n    3 - Siirtymä-graafi\n    0 - Sulje ohjelma\n\nValitse edellisistä: "))

import csv
import matplotlib.pyplot as plt


with open('hissidata.csv', mode = 'r') as hissidata:
    data = csv.reader(hissidata)
    time = [0]
    acc = [0]
    for row in data:
        try:
            time.append(float(row[0]))
            acc.append(float(row[1]))
        except ValueError:
            pass

    plt.xlabel('t (s)')
    plt.ylabel('a (m/s$^{2}$)')
    plt.plot(time,acc)
    plt.show()

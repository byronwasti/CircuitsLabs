import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import smu

s = smu.smu()
TAKE_NEW_DATA = False
FILENAME = "data/data.csv"


if TAKE_NEW_DATA:
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    Iin = np.logspace(-9, -2, 1000)[::-1]
    #V = np.logspace(
    vout = []
    for i in Iin:
        s.set_current(1, i)
        s.autorange(1)
        vout.append(s.get_voltage(1))

    s.set_current(1, 0.)

    x = Iin
    y = vout
    data = zip(x, y)
    writer.writerows(data)
    f.close()


if not TAKE_NEW_DATA:
    f = open(FILENAME, "rb")
    reader = csv.reader(f, ',')
    x = []
    y = []
    for row in reader:
        x.append[row[0]]
        y.append[row[1]]


if True:
    plt.semilogx(x, y, '.')
    plt.show()



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

TAKE_NEW_DATA = True
FILENAME = "data/data.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    #Iin = np.logspace(-9, -2, 100)[::-1]
    Vin = np.linspace(0.2, 0.8, 100)

    #vout = []
    iout = []
    for i in Vin:
        #s.set_current(1, i)
        s.set_voltage(1, i)
        s.autorange(1)
        #vout.append(s.get_voltage(1))
        iout.append(s.get_current(1))

    s.set_voltage(1, 0.)

    #x = Iin
    #y = vout
    x = Vin
    y = iout
    data = zip(x, y)
    writer.writerows(data)
    f.close()


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y = []
        for row in reader:
            x.append(row[0])
            y.append(row[1])


if True:
    plt.semilogy(x, y, '.')
    plt.show()



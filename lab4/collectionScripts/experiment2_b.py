import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment2_x_K_3.csv" #

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    ix = np.logspace(-8, -3, 250)
    #ix = np.linspace(1e-8, 1e-3, 200)
    iz = []

    #s.set_voltage(2, 0.)
    for i in ix:
        s.set_current(1, i)

        s.autorange(1)
        s.autorange(2)
    
        cur2 = s.get_current(2)

        iz.append(cur2)

    s.set_current(1, 0.)
    s.set_voltage(2, 0.)

    data = zip(ix, iz)
    writer.writerow(["I_x(Ch1)", "I_z(Ch2)"])
    writer.writerows(data)
    f.close()

    x = ix
    y = iz


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y = []

        for i, row in enumerate(reader):
            if i == 0 : continue
            x.append(row[0])
            y.append(row[1])


if True:
    fig, ax1 = plt.subplots()
    ax1.plot(x, y, '.', label="i_z")
    ax1.set_xlabel("Ix Current")
    ax1.set_ylabel("Iz Current")

    plt.show()

    #plt.plot(x, y1, '.', label="i_b")
    #plt.plot(x, y2, '.', label="i_e")
    #plt.legend()
    #plt.xlabel("Voltage")
    #plt.ylabel("Current")
    #plt.show()



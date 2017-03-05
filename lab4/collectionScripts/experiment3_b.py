'''
Stepwise vary I_x and sweep I_y
V_in @ 4.01V
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment3_x_200K_3.csv" #2K, 20K, 200K  ; @ 4V V_in

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    iy = -np.logspace(-8, -3, 250)
    iz = []

    #s.set_voltage(2, 0.)
    for i in iy:
        s.set_current(1, i)

        s.autorange(1)
        s.autorange(2)
    
        cur2 = s.get_current(2)

        iz.append(cur2)

    s.set_current(1, 0.)
    s.set_voltage(2, 0.)

    data = zip(iy, iz)
    writer.writerow(["I_y(Ch1)", "I_z(Ch2)"])
    writer.writerows(data)
    f.close()

    x = iy
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


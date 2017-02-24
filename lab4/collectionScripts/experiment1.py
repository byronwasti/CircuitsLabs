import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment1_Transistor4_3.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    vin = np.linspace(0.35, 1.2, 400)
    ib = []
    ie = []

    s.set_voltage(2, 0.)
    for v in vin:
        s.set_voltage(1, v)

        s.autorange(1)
        s.autorange(2)
    
        cur1 = s.get_current(1)
        cur2 = -s.get_current(2)

        ib.append(cur1)
        ie.append(cur2)

#        auto1 = s.get_autorange(1)
#        auto2 = s.get_autorange(2)
#        vrange1 = s.get_irange(1)
#        vrange2 = s.get_irange(2)

        #print(auto1, auto2, vrange1, vrange2, cur1, cur2, v)

    s.set_voltage(1, 0.)

    data = zip(vin, ib, ie)
    writer.writerow(["V_in(Ch1)", "I_b(Ch1)", "I_e(Ch2)"])
    writer.writerows(data)
    f.close()

    x = vin
    y1 = ib
    y2 = ie


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y1 = []
        y2 = []

        for i, row in enumerate(reader):
            if i == 0 : continue
            x.append(row[0])
            y1.append(row[1])
            y2.append(row[2])


if True:
    fig, ax1 = plt.subplots()
    ax1.plot(x, y1, '.', label="i_b")
    ax1.set_xlabel("Voltage")

    ax2 = ax1.twinx()
    ax2.plot(x, y2, '.', label="i_e")

    plt.show()

    #plt.plot(x, y1, '.', label="i_b")
    #plt.plot(x, y2, '.', label="i_e")
    #plt.legend()
    #plt.xlabel("Voltage")
    #plt.ylabel("Current")
    #plt.show()



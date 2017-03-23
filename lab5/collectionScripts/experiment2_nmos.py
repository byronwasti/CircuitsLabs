import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment2_nmos_1_Take2.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    vin = np.linspace(0, 5, 500)
    ichannel = []

    for v in vin:
        s.set_voltage(1, v)
        s.autorange(1)
        ichannel.append(-s.get_current(1))

    s.set_voltage(1, 0.)

    data = zip(vin, ichannel)
    writer.writerow(["V_source", "I_channel"])
    writer.writerows(data)
    f.close()

    x = vin
    y1 = ichannel


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y1 = []

        for i, row in enumerate(reader):
            if i == 0 : continue
            x.append(row[0])
            y1.append(row[1])


if True:

    plt.plot(x, y1, '.', label="i_channel")
    plt.xlabel("Voltage")
    plt.ylabel("Current")

    plt.show()


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment2_pmos_3.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    vin = np.linspace(-5, 0, 500)
    ichannel = []

    for v in vin:
        s.set_voltage(1, v)
        s.autorange(1)
        ichannel.append(s.get_current(1))

    s.set_voltage(1, 0.)

    data = zip(vin, ichannel)
    writer.writerow(["V_gate", "I_channel"])
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
    fig, ax1 = plt.subplots()

    ax1.plot(x, y1, '.', label="i_channel")
    ax1.set_xlabel("Voltage")
    ax1.set_ylabel("Current")

    plt.show()


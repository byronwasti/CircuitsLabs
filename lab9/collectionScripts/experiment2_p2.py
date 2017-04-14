import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/exp2_data2_CVC.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    v_out = np.linspace(0, 5, 200)
    i_out = []

    s.set_voltage(1, -0.01)
    for n in  v_out:
        s.set_voltage(2, n)

        s.autorange(1)
        s.autorange(2)
    
        i_out.append(s.get_current(2))

    s.set_voltage(2, 0.)
    s.set_voltage(1, 0.)

    data = zip(v_out, i_out)
    writer.writerow(["V_out", "I_out"])
    writer.writerows(data)
    f.close()

    x = v_out
    y1 = i_out


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
    ax1.set_xlabel("Voltage Out")
    ax1.set_ylabel("Current Out")

    plt.show()



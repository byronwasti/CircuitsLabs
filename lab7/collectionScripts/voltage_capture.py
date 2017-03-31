import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/strong_V2-3V_V_3.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    v_in = np.linspace(-2, 2, 200)
    v_out = []

    s.set_current(2, 0.)
    for n in  v_in:
        s.set_voltage(1, n)

        s.autorange(1)
        s.autorange(2)
    
        v_out.append(s.get_voltage(2))

    s.set_voltage(1, 0.)

    data = zip(v_in, v_out)
    writer.writerow(["V_input", "V"])
    writer.writerows(data)
    f.close()

    x = v_in
    y1 = v_out


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
    ax1.set_xlabel("Voltage In")
    ax1.set_ylabel("Voltage Out")

    plt.show()



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

TAKE_NEW_DATA = True
FILENAME = "../data/experiment3_current_divider_b_3.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    i_in = np.linspace(0, 15e-3, 100)
    i_out = []

    s.set_voltage(2, 0.)
    for i in i_in:
        s.set_current(1, i)

        s.autorange(1)
        s.autorange(2)
    
        i_out.append(s.get_current(2))

    s.set_current(1, 0.)
    s.set_voltage(2, 0.)

    data = zip(i_in, i_out)
    writer.writerow(["I_input", "I_output"])
    writer.writerows(data)
    f.close()

    x = i_in
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
    ax1.set_xlabel("Current In")
    ax1.set_ylabel("Current Out")

    plt.show()



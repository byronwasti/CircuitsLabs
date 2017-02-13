import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

TAKE_NEW_DATA = True
FILENAME = "data/experiment2_100K_3.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    v_in = np.linspace(0.0, 5, 255)
    i_b = []
    i_e = []

    s.set_voltage(2, 0.)
    for v in v_in:
        s.set_voltage(1, v)
        s.autorange(1)
        s.autorange(2)
        i_b.append(s.get_current(1))
        i_e.append(-s.get_current(2))

    s.set_voltage(1, 0.)

    data = zip(v_in, i_b, i_e)
    writer.writerow(["V_in(Ch1)", "I_b(Ch1)", "I_e(Ch2)"])
    writer.writerows(data)
    f.close()

    x = v_in
    y1 = i_b
    y2 = i_e


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y1 = []
        y2 = []
        for i, row in enumerate(reader):
            if i == 0: continue
            x.append(row[0])
            y1.append(row[1])
            y2.append(row[2])


if True:
    plt.plot(x, y1, '.', label="i_b")
    plt.legend()
    plt.figure()
    plt.plot(x, y2, '.', label="i_e")
    plt.legend()
    plt.xlabel("Voltage")
    plt.ylabel("Current")
    plt.show()



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

TAKE_NEW_DATA = True
FILENAME = "data/experiment3_1K_4.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()
    
    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    v_b = np.linspace(0.0, 5, 255)
    v_e = []

    for v in v_b:
        s.set_voltage(1, v)
        s.autorange(1)
        s.autorange(2)

        v_e.append(s.get_voltage(2))

    s.set_voltage(1, 0.)

    data = zip(v_b, v_e)
    writer.writerow(["V_in(Ch1)", "V_out(Ch2)"])
    writer.writerows(data)
    f.close()

    x = v_b
    y1 = v_e


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y1 = []
        for i, row in enumerate(reader):
            if i == 0: continue
            x.append(row[0])
            y1.append(row[1])

if True:
    plt.plot(x, y1, '.', label="V")
    plt.xlabel("Voltage")
    plt.ylabel("Voltage")
    plt.show()



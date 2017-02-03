import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

TAKE_NEW_DATA = True
FILENAME = "data/data.csv"

if TAKE_NEW_DATA:
    import smu
    s = smu.smu()

    s.set_function(1, 0) # SV/MI
    s.set_function(2, 1) # SI/MV

    f = open(FILENAME, "wb")
    writer = csv.writer(f)

    Vin = np.linspace(0, 2, 200)
    iout = []
    vout = []
    for i in Vin:
        s.set_voltage(1, i)
        s.autorange(1)
        s.autorange(2)
        iout.append(s.get_current(1))
        vout.append(s.get_voltage(2))

    s.set_voltage(1, 0.)

    x = Vin
    y1 = iout
    y2 = vout

    data = zip(x, y1, y2)
    writer.writerow(["Vin", "Iout", "V_diode"])
    writer.writerows(data)
    f.close()


if not TAKE_NEW_DATA:
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        x = []
        y1 = []
        y2 = []
        for i, row in enumerate(reader):
            if i == 0: continue # Labels
            x.append(row[0])
            y1.append(row[1])


if True:
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y1, '.', label="Current")
    ax2.plot(x, y2, '.', label="Voltage")
    plt.show()


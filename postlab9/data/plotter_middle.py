import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def getData(FILENAME):
    x = []
    y1 = []
    y2 = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0])*1e6)
            y1.append(float(row[1]))
            y2.append(float(row[2]))

    return np.array(x), np.array(y1), np.array(y2)

if __name__ == "__main__":
    t, V1, Vout = getData("middle.txt")
    plt.plot(t, V1, label="$V_1$")
    plt.plot(t, Vout, label="$V_{out}$")

    plt.title("Middle-Rail Step Response")
    plt.xlabel("Time ($\mu$s)")
    plt.ylabel("Voltage (V)")
    plt.legend()

    plt.text(2, 2.53, "Time Constant:\n$\\tau$ = %f $\mu$s" % 0.26 )

    plt.show()


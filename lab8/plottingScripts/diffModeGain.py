import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def getData(FILENAME):
    x = []
    y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]))
            y.append(float(row[1]))

    return np.array(x), np.array(y)


def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)


def plot():
    plt.xlabel("$V_{dm}$")
    plt.ylabel("$V_{out}$")
    plt.title("Weak VTC")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    v_in, v_out = getData("../data/exp2_data1_diffModeGain_1.csv")

    plotStuff( v_in, v_out, "Experimental Data" )

    plot()

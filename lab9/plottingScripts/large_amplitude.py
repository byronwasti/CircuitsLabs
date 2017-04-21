import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def getData(FILENAME):
    x = []
    y1 = []
    y2 = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]))
            y1.append(float(row[1]))
            y2.append(float(row[2]))

    return np.array(x), np.array(y1), np.array(y2)

def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def plot():
    plt.xlabel("Time (s)", fontsize=16)
    plt.ylabel("Voltage (V)", fontsize=16)
    plt.title("Slew-Rate / Large Amplitude Step", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

if __name__ == "__main__":
    time, v_in, v_out = getData("../data/exp3_large_amp.csv")

    plotStuff( time, v_in, "Input Step" )
    plotStuff( time, v_out, "Step Response" )

    plt.text(-0.0016, 3, "Slew Rates:\nRising Slew-Rate: %e V/s\nFalling Slew-Rate: %e V/s" % (37574.01, -36342.8233) )

    plot()

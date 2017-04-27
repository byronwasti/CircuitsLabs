import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def getData(FILENAME):
    x = []
    y1 = []
    y2 = []
    y3 = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]) * 1e6)
            y1.append(float(row[1]) * 1e6)
            y2.append(float(row[2]) * 1e6)
            y3.append(float(row[3]) * 1e6)

    return np.array(x), np.array(y1), np.array(y2), np.array(y3)

def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def plot():
    plt.xlabel("Time ($\mu$s)", fontsize=16)
    plt.ylabel("Current ($\mu$A)", fontsize=16)
    plt.title("Subtractor Circuit", fontsize=20)
    plt.legend(fontsize=20, loc='best')
    plt.show()

if __name__ == "__main__":
    time, i1, i2, iout = getData("../data/subtractor.txt")

    plotStuff( time, i1, "$I_1$" )
    plotStuff( time, i2, "$I_2$" )
    plotStuff( time, iout, "$I_{out}$" )

    plot()

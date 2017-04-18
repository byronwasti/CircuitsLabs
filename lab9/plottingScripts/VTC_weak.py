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
    plt.xlabel("$V_{in}$ (V)", fontsize=16)
    plt.ylabel("$V_{out}$ (V)", fontsize=16)
    plt.title("VTC", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

if __name__ == "__main__":
    v_in1, v_out1 = getData("../data/weak_VTC_V2=2.5V.csv")
    v_in2, v_out2 = getData("../data/weak_VTC_V2=3.25V.csv")
    v_in3, v_out3 = getData("../data/weak_VTC_V2=4V.csv")

    plotStuff( v_in1, v_out1, "$V_2 = 2.5V$" )
    plotStuff( v_in2, v_out2, "$V_2 = 3.25V$" )
    plotStuff( v_in3, v_out3, "$V_2 = 4V$" )

    plot()

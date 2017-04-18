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

def makeFit( x, y, start, end, label):
    fit = np.polyfit( x[start:end], y[start:end], 1)

    fit_func = lambda x: fit[0]*x + fit[1]

    plt.plot(x, [ fit_func(i) for i in x ], '-', label=label)
    plt.ylim(-0.1, 5.1)

    return fit

def plot():
    plt.xlabel("$V_{dm}$ (V)", fontsize=16)
    plt.ylabel("$V_{out}$ (V)", fontsize=16)
    plt.title("Differential-Mode Voltage Gain", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

if __name__ == "__main__":
    v_in, v_out = getData("../data/exp2_data1_diffModeGain.csv")

    plotStuff( v_in, v_out, "Experimental Data" )
    start, end = (63, 98)
    fit = makeFit( v_in, v_out, start, end, "Fit" )

    plt.text(0.005, 3.5, "Fit: ax + b\na=%e\nb=%e$V$" % (fit[0], fit[1]) )

    plot()

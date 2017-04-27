import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def getData(FILENAME):
    x = []
    y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]))
            y.append(float(row[3]))

    return np.array(x), np.array(y)


def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def makeFit( x, y, label):
    fit = np.polyfit( x, y, 1)

    fit_func = lambda x: fit[0]*x + fit[1]

    plt.plot(x, [ fit_func(i) for i in x ], '-', label=label)

    return fit

def plot():
    plt.xlabel("$V_{dm}$")
    plt.ylabel("$V_{out}$")
    plt.title("Differential-Mode Voltage Gain")
    plt.axis([-0.25, 0.25, 0, 5])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    v_in, v_out = getData("../data/adaptive-biasing-V3_DiffModeGain.txt")

    plotStuff( v_in, v_out, "Experimental Data" )
    start, end = (len(v_in)//2 - 25, len(v_in)//2 + 10)
    fit = makeFit( v_in[start:end], v_out[start:end], "Fit" )

    plt.text(0, 2, "Fit: ax + b\na=%e\nb=%e$V$" % (fit[0], fit[1]) )

    plot()

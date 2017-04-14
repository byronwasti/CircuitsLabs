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

def makeFit( x, y, label):
    fit = np.polyfit( x, y, 1)

    fit_func = lambda x: fit[0]*x + fit[1]

    plt.plot(x, [ fit_func(i) for i in x ], '-', label=label)

    return fit

def plot():
    plt.xlabel("$V_{out}$")
    plt.ylabel("$I_{out}$")
    plt.title("Incremental Output Resistance")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    v_in, v_out = getData("../data/exp2_data2_CVC.csv")

    plotStuff( v_in, v_out, "Experimental Data" )
    start, end = (70, 200)
    fit = makeFit( v_in[start:end], v_out[start:end], "Fit" )

    plt.text(2, -0.0005, "Fit: ax + b\na=%e$\mho$\nb=%e$A$\n\n$r_0$=1/a=%e$\Omega$" % (fit[0], fit[1], 1/fit[0]) )

    plot()

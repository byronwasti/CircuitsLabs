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
            x.append(float(row[2]))
            y.append(-float(row[3]))

    return np.array(x), np.array(y)


def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def makeFit( x, y, label):
    fit = np.polyfit( x, y, 1)

    fit_func = lambda x: fit[0]*x + fit[1]

    plt.plot(x, [ fit_func(i)*1e6 for i in x ], '-', label=label)

    return fit

def plot():
    plt.xlabel("$V_{out}$ (V)", fontsize=16)
    plt.ylabel("$I_{out}$ ($\mu$A)", fontsize=16)
    plt.title("Incremental Output Resistance", fontsize=18)
    plt.legend(fontsize=16)
    plt.show()

if __name__ == "__main__":
    v_out, i_out = getData("../data/adaptive-biasing-V3_Rout.txt")

    plotStuff( v_out, i_out*1e6, "Experimental Data" )
    start, end = (50, 400)
    fit = makeFit( v_out[start:end], i_out[start:end], "Fit" )

    plt.text(2, 5, "Fit: ax + b\na=%e$\mho$\nb=%e$A$\n\n$r_0$=1/a=%e$\Omega$" % (fit[0], fit[1], 1/fit[0]) )

    plot()

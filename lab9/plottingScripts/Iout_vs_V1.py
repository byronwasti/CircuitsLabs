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
            if i == 0: continue
            x.append(float(row[0]))
            y.append(float(row[1]))
    
    return np.array(x), np.array(y)


def plot_IvsV1(v_x, i_y, label):
    
    plt.plot(v_x, i_y, '.', label=label)


def makeFit(v_x, i_y, start, end, label):
    
    fit = np.polyfit(v_x[start:end], i_y[start:end], 1)
    fit_func = lambda x: fit[0]*x + fit[1]
    plt.plot(v_x, [fit_func(i) for i in v_x], label=label)
    plt.text(0.1, -0.000005, "Fit: ax + b\na=%e$\mho$\nb=%e$A$" % (fit[0], fit[1]))


if __name__ == "__main__":
    v_x, i_y = getData("../data/exp2_data3_CVC_diff.csv")
    
    plot_IvsV1(v_x, i_y, "Experimental Data")
    
    start, end = (270, 330)
    makeFit(v_x, i_y, start, end, "Theoretical Fit")
    
    plt.ylim(-0.00005, 0.00005)
    plt.xlabel("$V_{dm}$", fontsize=16)
    plt.ylabel("$I_{out}$ (A)", fontsize=16)
    plt.title("$I_{out}$ vs. $V_{dm}$", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

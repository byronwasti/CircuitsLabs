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
            if i == 0: continue
            x.append(float(row[0]))
            y.append(float(row[4]))
    
    return np.array(x), np.array(y)


def plot_IvsV1(v_x, i_y, label):
    
    plt.plot(v_x, i_y, '.', label=label)


def makeFit(v_x, i_y, start, end, label):
    
    fit = np.polyfit(v_x[start:end], i_y[start:end], 1)
    fit_func = lambda x: fit[0]*x + fit[1]
    #plt.plot(v_x, [fit_func(i) for i in v_x], label=label)
    plt.plot(v_x[start:end], [fit_func(i)*1e6 for i in v_x[start:end] ] )
    plt.text(0.1, -25, "Fit: ax + b\na=%e$\mho$\nb=%e$A$" % (fit[0], fit[1]))


if __name__ == "__main__":
    v_x, i_y = getData("../data/adaptive-biasing-V3_Gm.txt")
    
    plot_IvsV1(v_x, i_y*1e6, "Experimental Data")
    
    start, end = (120, 350)
    #start, end = (0, len(i_y)-1)
    makeFit(v_x, i_y, start, end, "Theoretical Fit")
    
    plt.xlabel("$V_{dm}$", fontsize=16)
    plt.ylabel("$I_{out}$ ($\mu$A)", fontsize=16)
    plt.title("$G_{m}$", fontsize=20)
    plt.show()

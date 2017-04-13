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


def plot_VvsV(v_x, v_y, label):
    
    plt.plot(v_x, v_y, '.', label=label)


def makeFit(v_x, v_y, start, end, label):
    
    fit = np.polyfit(v_x[start:end], v_y[start:end], 1)
    fit_func = lambda x: fit[0]*x + fit[1]
    plt.plot(v_x, [fit_func(i) for i in v_x], label=label)
    plt.text(1.6, 1, "Fit: ax + b\na=%e\nb=%e$V$" % (fit[0], fit[1]))

if __name__ == "__main__":
    v_x, v_y = getData("../data/exp3_unityGain_data2_1.csv")
    
    plot_VvsV(v_x, v_y, "Experimental Data")
    
    start, end = (10, 230)
    # makeFit(v_x, v_y, start, end, "Theoretical Fit")
    
    plt.xlabel("$V_{in}$ (V)", fontsize=16)
    plt.ylabel("$V_{out}$ - $V_{in}$ (V)", fontsize=16)
    plt.title("$V_{out}$ - $V_{in}$ vs. $V_{in}$", fontsize=20)
    plt.show()

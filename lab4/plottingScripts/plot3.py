import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def plotBeta(FILENAME, count):
    v_in = []
    i_b = []
    i_c = []
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            #if float(row[0]) > 0.65 : continue
            #if float(row[0]) < 0.4 : continue
            v_in.append(float(row[0]))
            i_b.append(float(row[1]))
            i_c.append(float(row[2]) - float(row[1]))

    # Fits
    log_i_b = np.log(i_b)
    log_i_c = np.log(i_c)

    fit = np.polyfit(v_in, log_i_c, 1)
    Is = np.exp(fit[1])
    UT = 1/fit[0]
    p = [ Is * np.exp(V / UT) for V in v_in ]

    # beta extraction
    ib_ic_diff = np.divide(i_c, i_b)
    #beta = np.mean(ib_ic_diff)

    # Plotting

    plt.semilogy(i_b, ib_ic_diff, '.', label=count)

    plt.xlabel("Base Current (A)")
    plt.ylabel("$\\beta$")
    plt.title("$\\beta$ as a Function of Base Current")
    plt.legend()
    return

if __name__ == "__main__":
    plotBeta("../data/experiment1_Transistor1_1.csv", "Transistor 1")
    plotBeta("../data/experiment1_Transistor2_1.csv", "Transistor 2")
    plotBeta("../data/experiment1_Transistor3_1.csv", "Transistor 3")
    plotBeta("../data/experiment1_Transistor4_1.csv", "Transistor 4")
    plt.show()

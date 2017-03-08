'''
Table
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def extractParams(FILENAME):
    v_in = []
    i_b = []
    i_c = []
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            if float(row[0]) > 0.65 : continue
            if float(row[0]) < 0.4 : continue
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
    beta = np.mean(ib_ic_diff)

    # Plotting
    plt.figure()

    plt.semilogy(v_in, i_c, '.', label="Collector Current")
    plt.semilogy(v_in, p, '-', label="Collector Current")
    plt.semilogy(v_in, i_b, '.', label="Base Current")


    plt.xlabel("Base Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Current vs. Base Voltage")
    plt.legend()

    return Is, UT, beta

if __name__ == "__main__":
    Is, UT, beta = extractParams("../data/experiment1_Transistor1_1.csv")
    print("%e, %e, %e" % (Is, UT, beta))

    Is, UT, beta = extractParams("../data/experiment1_Transistor2_1.csv")
    print("%e, %e, %e" % (Is, UT, beta))

    Is, UT, beta = extractParams("../data/experiment1_Transistor3_1.csv")
    print("%e, %e, %e" % (Is, UT, beta))

    Is, UT, beta = extractParams("../data/experiment1_Transistor4_1.csv")
    print("%e, %e, %e" % (Is, UT, beta))

    #plt.show()


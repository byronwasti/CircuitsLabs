import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def getData(FILENAME):
    vgate = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vgate.append(float(row[0]))
            ichannel.append(float(row[1]))

    return np.array(vgate), np.array(ichannel)

def plotRatio(vgate, ratio, label):
    plt.plot(vgate, ratio, '.', label=label)

def plot():
    plt.axis([0, 5.1, 0, 3])
    plt.xlabel("Gate Voltage (V)")
    plt.ylabel("Ratio")
    plt.title("nMOS Series and Parallel Ratios for 5V Drain")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    vgate_single, ichannel_single = getData("../data/experiment2_single_transistor_5v_1.csv")
    vgate_parallel, ichannel_parallel = getData("../data/experiment2_parallel_transistor_5V_2.csv")
    vgate_series, ichannel_series = getData("../data/experiment2_series_transistor_5v_1.csv")

    ratio_parallel = ichannel_parallel/ichannel_single
    ratio_series = ichannel_series/ichannel_single

    plotRatio(vgate_single, ratio_series, "Series Ratio")
    plotRatio(vgate_single, ratio_parallel, "Parallel Ratio")

    plot()

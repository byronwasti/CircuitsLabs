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


def plotStuff( vgates, ichannels, labels):
    for i in range(3):
        plt.semilogy(vgates[i], ichannels[i], '.', label=labels[i])

def plot():
    plt.xlabel("Gate Voltage (V)")
    plt.ylabel("Channel Current (A)")
    plt.title("nMOS Series and Parallel Characteristic for 5V Drain")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    vgate_single, ichannel_single = getData("../data/experiment2_single_transistor_5v_1.csv")
    vgate_parallel, ichannel_parallel = getData("../data/experiment2_parallel_transistor_5V_1.csv")
    vgate_series, ichannel_series = getData("../data/experiment2_series_transistor_5v_1.csv")

    plotStuff( [vgate_single, vgate_parallel, vgate_series], [ichannel_single, ichannel_parallel, ichannel_series], ["Single", "Parallel", "Series"] )

    plot()

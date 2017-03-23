import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def plot_things(FILENAME, label):
    vdrain = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vdrain.append(float(row[0]))
            ichannel.append(float(row[1]))

    plt.semilogy(vdrain, ichannel, '.', label=label)


def plotNMOS():
    plot_things("../data/experiment3_nmos_weak_3.csv", "weak")
    plot_things("../data/experiment3_nmos_moderate_3.csv", "moderate")
    plot_things("../data/experiment3_nmos_strong_2.csv", "strong")


if __name__ ==  "__main__":

    plotNMOS()

    plt.title("nMOS Drain Characteristics")
    plt.xlabel("Drain Voltage (V)")
    plt.ylabel("Channel Current (A)")
    plt.legend()
    plt.show()

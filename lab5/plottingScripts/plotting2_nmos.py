import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def plot_things(FILENAME, label):
    vsource = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vsource.append(float(row[0]))
            ichannel.append(float(row[1]))

    plt.semilogx(vsource, ichannel, '.', label=label)


if __name__ == "__main__":

    plot_things("../data/experiment2_nmos_1.csv", "")
    plt.show()

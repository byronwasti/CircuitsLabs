import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def getInputData(FILENAME):
    x = []
    y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]))
            y.append(float(row[1]))

    return np.array(x), np.array(y)


def getOutputData(FILENAME):
    x = []
    y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]))
            y.append(float(row[2]))

    return np.array(x), np.array(y)


def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)


def plot():
    plt.xlabel("Time (s)", fontsize=16)
    plt.ylabel("$V_{out}$ (V)", fontsize=16)
    plt.title("Unity Gain Follower Step Response, Large Amplitude", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

    
if __name__ == "__main__":
    v1_in, v1_out = getInputData("../data/exp3_large_amp.csv")
    v2_in, v2_out = getOutputData("../data/exp3_large_amp.csv")

    plotStuff( v1_in, v1_out, "Input Waveform" )
    plotStuff( v2_in, v2_out, "Output Waveform" )
    plot()

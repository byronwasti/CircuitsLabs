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
    plt.xlabel("Time (s)", fontsize=20)
    plt.ylabel("$V_{out}$ (V)", fontsize=20)
    plt.title("Unity Gain Follower Step Response, Small Amplitude", fontsize=22)
    plt.legend(fontsize=16, loc='best')
    plt.show()

    
if __name__ == "__main__":
    v1_in, v1_out = getInputData("../data/exp3_small_amp_2.csv")
    v2_in, v2_out = getOutputData("../data/exp3_small_amp_2.csv")
    
    start, end = (2300, 4300)
    plotStuff( v1_in[start:end], v1_out[start:end], "Input Waveform" )
    plotStuff( v2_in[start:end], v2_out[start:end], "Output Waveform" )
    plt.text(-0.0008, 2.55, "Time Constants:\nFalling Time Constant: -5.78591094e-6 s\nRising Time Constant: 5.49265088e-6 s", fontsize=16)
    plot()

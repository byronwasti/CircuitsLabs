import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def getData(FILENAME):
    x = []
    y1 = []
    y2 = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            if i==0 : continue
            x.append(float(row[0]) * 1e6)
            y1.append(float(row[1]))
            y2.append(float(row[2]))

    return np.array(x), np.array(y1), np.array(y2)

def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def plot():
    plt.xlabel("Time ($\mu$s)", fontsize=16)
    plt.ylabel("Voltage (V)", fontsize=16)
    plt.title("Slew Rate Postlab9 Circuit", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

if __name__ == "__main__":
    time, v_in, v_out = getData("../data/postlab9.txt")

    plotStuff( time, v_in, "Input Step" )
    plotStuff( time, v_out, "Step Response" )

    plt.text(2, 2, "Rising Slew Rate: %e\nFalling Slew Rate: %e" % (2545415.57010371, -2572342.230633689) )


    time, v_in, v_out = getData("../data/adaptive-biasing.txt")
    plotStuff( time, v_in, "Input Step" )
    plotStuff( time, v_out, "Step Response" )

    plot()

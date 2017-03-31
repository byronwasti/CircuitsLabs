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
            if i==0 : continue
            x.append(-float(row[0]))
            y.append(float(row[1]))

    return np.array(x), np.array(y)


def plot():
    plt.xlabel("Input Current (A)")
    plt.ylabel("Output Current (A)")
    plt.title("nMOS Current Divider (a)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    iin, iout = getData("../data/experiment3_current_divider_a_1.csv")
    
    theoretical = [ i/2 for i in iin ]
    plt.plot(iin, iout, '.', label="Experimental Data")
    plt.plot(iin, theoretical, '-', label="Theoretical")


    fit = np.polyfit(iin, iout, 1)
    plt.text(0.006, 0.002, "Experimental Divider Ratio: %e\nTheoretical Divider Ratio: 0.5" % fit[0])


    plot()

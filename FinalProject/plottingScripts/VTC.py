import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def getData(FILENAME):
    x = [ [], [], [], [] ]
    y1 = [ [], [], [], [] ]
    y2 = []
    
    part = -1
    takeNew = True
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            if i==0 : continue

            if row[0].startswith("Step"):
                part += 1
                takeNew = True
                continue 

            x[part].append(float(row[0]))
            y1[part].append(float(row[3]))

            if takeNew:
                y2.append(float(row[2]))
                takeNew = False

    return np.array(x), np.array(y1), np.array(y2)

def plotStuff( x, y, label):
    plt.plot(x, y, '.',  label=label)

def plot():
    plt.xlabel("$V_{1}$ (V)", fontsize=16)
    plt.ylabel("$V_{out}$ (V)", fontsize=16)
    plt.title("Adaptive-Biasing VTC", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

if __name__ == "__main__":
    v_1, v_out, v_2 = getData("../data/adaptive-biasing-V3_VTC.txt")
    
    for i, val in enumerate(v_2):
        plotStuff( v_1[i], v_out[i], "$V_2$ = %f" % val)

    plot()


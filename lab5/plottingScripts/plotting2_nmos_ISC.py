import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def data(FILENAME):
    vsource = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vsource.append(float(row[0]))
            ichannel.append(float(row[1]))

    return np.array(vsource), -np.array(ichannel)

def ISC(vsource, ichannel):
    gs = np.divide( np.diff(ichannel) , np.diff(vsource) )

    #plt.plot(ichannel)
    #plt.plot(gs)
    plt.plot(ichannel[:-1], gs, '.')

if __name__ == "__main__":
    vsource, ichannel = data("../data/experiment2_nmos_3.csv")
    ISC(vsource, ichannel)

    plt.show()

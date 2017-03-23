import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def get_data(FILENAME):
    vdrain = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vdrain.append(float(row[0]))
            ichannel.append(float(row[1]))

    return np.array(vdrain), np.array(ichannel)


def intrinsic_gain(FILENAME):
    vdrain, ichannel = get_data(FILENAME)
    start = 0
    end = 20
    
    fit = np.polyfit(vdrain[start:end], np.log(ichannel[start:end]), 1)
    

if __name__ ==  "__main__":

    intrinsic_gain("../data/experiment3_nmos_weak_3.csv")

    plt.title("nMOS Drain Characteristics")
    plt.xlabel("Drain Voltage (V)")
    plt.ylabel("Channel Current (A)")
    plt.legend()
    plt.show()

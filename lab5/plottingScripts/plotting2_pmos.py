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

    ichannel = np.array(ichannel)
    plt.semilogy(np.array(vsource)+5, ichannel, '.', label=label)

    return zip(vsource, ichannel)

def plot_fit(data):
    vsource_orig = np.array([ i[0] for i in data if i[0] > -4 and i[0] < -3.4])

    data_filtered = [ i for i in data if i[0] > -3.8 and i[0] < -3.6 ]
    
    vsource = np.array([i[0] for i in data_filtered])
    ichannel = np.array([i[1] for i in data_filtered])

    log_ichannel = np.log(ichannel)

    fit = np.polyfit(vsource, log_ichannel, 1)
    theoretical = np.exp(fit[0]*vsource_orig)*np.exp(fit[1])

    plt.semilogy(vsource_orig+5, theoretical, '-', label='Theoretical')

    plt.text(0, 1e-4, "Fit ax + b\na=%e$\mho$\nb=%eA" % (fit[0], fit[1]) )
    print(fit)

if __name__ == "__main__":
    data = plot_things("../data/experiment2_pmos_3.csv", "pMOS Data")
    plot_fit(list(data))

    plt.legend()
    plt.xlabel("Source Voltage (V)")
    plt.ylabel("Channel Current (A)")
    plt.title("pMOS Source Characteristics")
    plt.show()

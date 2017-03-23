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


def early_voltage(FILENAME, limits):
    vdrain_o, ichannel_o = get_data(FILENAME)

    data = zip(vdrain_o, ichannel_o)
    data = [ i for i in data if i[0] > limits[0] and i[0] < limits[1] ]

    vdrain = [i[0] for i in data]
    ichannel = [i[1] for i in data]


    fit = np.polyfit(vdrain, np.log(ichannel), 1)
    
    v_early = 1/ (fit[0]) * fit[1]
    print(v_early)

    return -fit[1], -v_early

    #plt.figure()
    #plt.semilogy(vdrain_o, ichannel_o)
    #plt.semilogy(vdrain, ichannel)
    


if __name__ ==  "__main__":

    i_sat0, v_early0 = early_voltage("../data/experiment3_nmos_weak_3.csv", [ 0.5, 3 ])
    i_sat1, v_early1 = early_voltage("../data/experiment3_nmos_moderate_3.csv", [ 0.5, 3 ])
    i_sat2, v_early2 = early_voltage("../data/experiment3_nmos_strong_2.csv", [ 3, 5 ])

    plt.semilogx(i_sat0, v_early0, 'X', label="Weak Inversion")
    plt.semilogx(i_sat1, v_early1, 'X', label="Moderate Inversion")
    plt.semilogx(i_sat2, v_early2, 'X', label="Strong Inversion")

    plt.title("nMOS Early Voltage")
    plt.ylabel("Early Voltage (V)")
    plt.xlabel("$I_{sat}$ (A)")
    plt.legend()
    plt.show()

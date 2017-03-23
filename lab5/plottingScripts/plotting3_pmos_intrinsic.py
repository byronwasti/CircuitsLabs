import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

'''
381.07882912 Weak
429.508677578 Moderate
238.242477323 Strong

28.4340966001 Weak
35.9309957967 Moderate
45.2579748368 Strong

ISAT
13.4021781834
11.9537092712
5.264099381

'''

def get_data(FILENAME):
    vdrain = []
    ichannel = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0 : continue
            vdrain.append(float(row[0]))
            ichannel.append(-float(row[1]))

    return np.array(vdrain), np.array(ichannel)


def intrinsic_gain(FILENAME):
    vdrain, ichannel = get_data(FILENAME)
    start = -20
    fit = np.polyfit(vdrain[start:], np.log(ichannel[start:]), 1)
    gs = fit[0]
    print(fit)
    return fit[0]

if __name__ ==  "__main__":
    gs0 = intrinsic_gain("../data/experiment3_pmos_weak_4.csv")
    gs1 = intrinsic_gain("../data/experiment3_pmos_moderate_3.csv")
    gs2 = intrinsic_gain("../data/experiment3_pmos_strong_4.csv")

    #r0 = 28.4340966001
    #r1 = 35.9309957967
    #r2 = 45.2579748368
    #r0 = 3.00532251978
    #r1 = 10.8897839808
    #r2 = 20.2891567438


    #isat0 =13.4021781834
    #isat1 =11.9537092712
    #isat2 =5.264099381
    #isat0 = 15.916800824
    #isat1 = 14.5708546044
    #isat2 = 6.30076026395

    r0 = -98285563.6162
    isat0 = 7.32681806468e-08
    r1 = -34144906.2444
    isat1 = 4.42719190744e-07
    r2 = -11692.5543
    isat2 = 0.00183293208467



    plt.semilogx(isat0, gs0 * r0, 'X', label='Weak')
    plt.semilogx(isat1, gs1 * r1, 'X', label='Moderate')
    plt.semilogx(isat2, gs2 * r2, 'X', label='Strong')

    plt.title("pMOS Intrinsic Gain")
    plt.xlabel("Saturation Current (A)")
    plt.ylabel("Intrinsic Gain")
    plt.legend()
    plt.show()

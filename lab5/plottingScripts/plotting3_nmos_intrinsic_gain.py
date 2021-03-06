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
            ichannel.append(float(row[1]))

    return np.array(vdrain), np.array(ichannel)


def intrinsic_gain(FILENAME):
    vdrain, ichannel = get_data(FILENAME)
    start = 0
    end = 20
    
    fit = np.polyfit(vdrain[start:end], np.log(ichannel[start:end]), 1)
    gs = fit[0]
    print(fit)
    return fit[0]

if __name__ ==  "__main__":
    gs0 = intrinsic_gain("../data/experiment3_nmos_weak_3.csv")
    gs1 = intrinsic_gain("../data/experiment3_nmos_moderate_3.csv")
    gs2 = intrinsic_gain("../data/experiment3_nmos_strong_2.csv")

    r0 = 17791319.6087
    isat0 = 1.50994876476e-06

    r1 = 5349090.605
    isat1 = 6.43058326331e-06

    r2 = 8036.7388742
    isat2 = 0.00515494709913

    '''
    r0 = 28.4340966001
    r1 = 35.9309957967
    r2 = 45.2579748368

    isat0 =13.4021781834
    isat1 =11.9537092712
    isat2 =5.264099381
    '''

    plt.semilogx(isat0, gs0 * r0, 'X', label='Weak')
    plt.semilogx(isat1, gs1 * r1, 'X', label='Moderate')
    plt.semilogx(isat2, gs2 * r2, 'X', label='Strong')

    plt.title("nMOS Intrinsic Gain")
    plt.xlabel("Saturation Current (A)")
    plt.ylabel("Intrinsic Gain")
    plt.legend()
    plt.show()

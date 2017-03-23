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
    plt.loglog(ichannel[:-1], -gs, '.')

    U_T = 0.0258
    gs_weak = [ i/ U_T for i in ichannel[:-1] ]
    plt.loglog(ichannel[:-1], gs_weak, '-')

    plt.text(1e-7, 1e-6, "$I_{sat}/U_T$\nU_T=%eV" % U_T )

    I_s = 1.9361e-6
    gs_strong = [ np.sqrt(I_s * i)/U_T for i in ichannel[:-1] ]
    plt.loglog(ichannel[:-1], gs_strong)
    plt.text(1e-3, 1e-4, "$\\sqrt{I_sI_{sat}}/U_T$\nU_T=%eV\nI_s=%eA" % (U_T, I_s) )

if __name__ == "__main__":
    vsource, ichannel = data("../data/experiment2_nmos_2.csv")
    ISC(vsource, ichannel)
    
    plt.xlabel("Source Current (A)")
    plt.ylabel("Incremental Source Conductance")
    plt.title("nMOS Incremental Source Conductance")
    plt.show()

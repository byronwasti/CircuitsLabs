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
            x.append(float(row[0]))
            y.append(float(row[1]))

    return np.array(x), np.array(y)


def plotStuff( vdiff, idiff, label, fitlabel):
    plt.plot(vdiff, idiff, '.',  label=label)

    vdiff_f = []
    idiff_f = []
    for idx, val in enumerate(vdiff):
        if abs(val) < 0.05:
            vdiff_f.append(val)
            idiff_f.append( idiff[idx] )

    fit = np.polyfit(vdiff_f, idiff_f, 1)
    fit_i = [ fit[0]*v + fit[1] for v in vdiff ]
    plt.plot(vdiff, fit_i, '-', label=fitlabel)

    return fit
    #plt.plot(vdiff_f, idiff_f, '.', label= label + "_")


def plot():
    plt.xlabel("$V_1 - V_2$ (V) ")
    plt.ylabel("$I_1 - I_2$ (A)")
    plt.title("Differential-Mode Transconductance Gain")
    plt.axis([-0.3, 0.3, -3e-6, 3e-6])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    vdiff1_3V, i1_3V = getData("../data/weak_V2-3V_I1_1.csv")
    vdiff2_3V, i2_3V = getData("../data/weak_V2-3V_I2_1.csv")

    vdiff1_35V, i1_35V = getData("../data/weak_V2-3.5V_I1_1.csv")
    vdiff2_35V, i2_35V = getData("../data/weak_V2-3.5V_I2_1.csv")

    vdiff1_4V, i1_4V = getData("../data/weak_V2-4V_I1_1.csv")
    vdiff2_4V, i2_4V = getData("../data/weak_V2-4V_I2_1.csv")

    fit1 = plotStuff( vdiff1_3V, i1_3V - i2_3V, "Weak @ 3V", "Fit1: Fit for Weak @ 3V")
    fit2 = plotStuff( vdiff1_35V, i1_35V - i2_35V, "Weak @ 3.5V", "Fit2: Fit for Weak @ 3.5V")
    fit3 = plotStuff( vdiff1_4V, i1_4V - i2_4V, "Weak @ 4V", "Fit3: Fit for Weak @ 4V")

    plt.text(0.1, 0, "I = mV + b\nFit1: m=%eV b=%eA\nFit2: m=%eV b=%eA\nFit3: m=%eV b=%eA" % (fit1[0], fit1[1],fit2[0], fit2[1],fit3[0], fit3[1] ) )

    plot()

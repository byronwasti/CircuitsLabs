import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

VOL_VOL = "data/experiment3_1K_1.csv"
with open(VOL_VOL, 'r') as f:
    reader = csv.reader(f)
    Vin  = []
    Vout = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 35 : continue
        if i > 245: continue
        Vin.append(float(row[0]))
        Vout.append(float(row[1]))

fit1 = np.polyfit(Vin, Vout, 1)
poly = np.poly1d(fit1)
theoretical_VTC = lambda x: poly(Vin)

plt.plot(Vin, Vout, '.', label='$V_{out}$ vs. $V_{in}$')
plt.plot(Vin, theoretical_VTC(Vin), label='theoretical VTC')
plt.text(1.4, 2.5, '$V_{out}$ = %f$V_{in}$ - %fV' %(fit1[0], fit1[1]*-1))
plt.title('$V_{out}$ vs. $V_{in}$', fontsize=20)
plt.legend(fontsize=12, loc='best')
plt.xlabel('$V_{in}$', fontsize=16)
plt.ylabel('$V_{out}$', fontsize=16)
plt.show()

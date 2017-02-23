import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

CUR_VOL = "data/experiment1_data2_2.csv"
with open(CUR_VOL, 'r') as f:
    reader = csv.reader(f)
    Vin    = []
    Ibase  = []
    Iemit  = []
    Icoll  = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 80 : continue
        if i > 190 : continue
        Vin.append(float(row[0]))
        Ibase.append(float(row[1]))
        Iemit.append(float(row[2]))
        Icoll.append(float(row[2]) - float(row[1]))

#gm = dIcoll / dVin
gm = []
for i in range(len(Icoll)):
    gm.append(Icoll[i] / Vin[i])
        
fit1 = np.polyfit(np.log(Icoll), np.log(gm), 1)
U_T = fit1[1]
poly = np.poly1d(fit1)
theoretical_gm = lambda x: np.exp(poly(np.log(Icoll)))

plt.loglog(Icoll, gm, '.', label=r'$g_m$ vs. $I_c$')
plt.loglog(Icoll, theoretical_gm(Icoll), label=r'theoretical $g_m$ vs. $I_c$')
plt.text(0.7e-3, 1e-2, "$g_m = I_c / U_T$\n$U_T$=%eV" % (U_T))
plt.title(r'$g_m$ vs. $I_c$', fontsize=20)
plt.legend(fontsize=12)
plt.xlabel(r'$I_c$', fontsize=16)
plt.ylabel(r'$r_b$', fontsize=16)
plt.show()

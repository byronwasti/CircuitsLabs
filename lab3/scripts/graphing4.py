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
gm = np.diff(Icoll) / np.diff(Vin)
        
#fit1 = np.polyfit(np.log(Icoll), np.log(gm), 1)
#U_T = fit1[1]
#poly = np.poly1d(fit1)
UT = 2.6e-2
theoretical_gm = [ i / UT for i in Icoll[:-1] ]

plt.loglog(Icoll[:-1], gm, '.', label=r'$g_m$ vs. $I_c$')
plt.loglog(Icoll[:-1], theoretical_gm, label=r'theoretical $g_m$ vs. $I_c$')
plt.text(0.7e-3, 1e-2, "$g_m = I_c / U_T$\n$U_T$=%eV" % (UT))
plt.title(r'$g_m$ vs. $I_c$', fontsize=20)
plt.legend(fontsize=12)
plt.xlabel(r'$I_c$', fontsize=16)
plt.ylabel(r'$r_b$', fontsize=16)
plt.show()

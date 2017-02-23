import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

CUR_VOL = "data/experiment1_data2_2.csv"
with open(CUR_VOL, 'r') as f:
    reader = csv.reader(f)
    Vin   = []
    Ibase = []
    Iemit = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 50 : continue
        if i > 190 : continue
        Vin.append(float(row[0]))
        Ibase.append(float(row[1]))
        Iemit.append(float(row[2]))

#rbase = dVin / dIbase
rbase = np.diff(Vin)/np.diff(Ibase)
#for i in range(len(Ibase)):
#    rbase.append(Vin[i] / Ibase[i])

fit1 = np.polyfit(np.log(Ibase[:-1]), np.log(rbase), 1)

print(fit1)
poly = np.poly1d(fit1)
#theoretical_rbase = lambda x: np.exp(poly(np.log(x)))
UT = 2.8e-2
theoretical_rbase = [ UT / i for i in Ibase[:-1] ]
    
plt.loglog(Ibase[:-1], rbase, '.', label=r'$r_b$ vs. $I_{base}$')
plt.loglog(Ibase[:-1], theoretical_rbase, label=r'theoretical $r_b$ vs. $I_{base}$')
plt.text(1e-6, 1e6, '$r_b$ = $U_T$ / $I_B$ \n $U_T$=%eV' % UT )
plt.title(r'$r_b$ vs. $I_{base}$', fontsize=20)
plt.legend(fontsize=12)
plt.xlabel(r'$I_{base}$ (A)', fontsize=16)
plt.ylabel(r'$r_b$', fontsize=16)
plt.show()

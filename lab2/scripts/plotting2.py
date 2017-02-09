import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

VOL_CUR = "data/e1_cur_3_dense.csv"

with open(VOL_CUR, 'r') as f:
    reader = csv.reader(f)
    Iin = []
    Vout = []
    for row in reader:
        Iin.append(float(row[0]))
        Vout.append(float(row[1]))

r_d = np.diff(Vout)/np.diff(Iin)

def func(x, a):
    return a/x

popt, pcov = curve_fit(func, Iin[:-1], r_d, p0=(1e-2))
print(popt, pcov)
U_T = popt[0]
r_d_theoretical = [ U_T/x for x in Iin[:-1] ]


#U_T = 2.886611e-02
#r_d_theoretical = [ U_T/x for x in Iin[:-1] ]

plt.loglog(Iin[:-1], r_d, '.', label="Experimental")
plt.loglog(Iin[:-1], r_d_theoretical, '-', label="Theoretical")


plt.xlabel("Current (A)", fontsize=20)
plt.ylabel("Incremental Resistance ($\Omega$)", fontsize=20)
plt.title("Incremental Resistance vs. Current", fontsize=20)
plt.legend(fontsize=18)
plt.text(1e-5, 1e6, "Fit: $r_d = U_T/I$\n$U_T$=%e$\Omega A$" % U_T, fontsize=20)
#plt.plot(Iin, Vout, '.')
plt.show()

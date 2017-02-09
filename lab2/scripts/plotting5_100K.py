import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

RES = "100K"
VOL_CUR = "data/e2_res"+RES+"_2.csv"

with open(VOL_CUR, 'r') as f:
    reader = csv.reader(f)
    Vin = []
    Iout = []
    for i, row in enumerate(reader):
        if i == 0: continue
        Vin.append(float(row[0]))
        Iout.append(float(row[1]))

#r_d = np.diff(Vout)/np.diff(Iin) 
#U_T = 2.886611e-02
#r_d_theoretical = [ U_T/x for x in Iin[:-1] ]

fit = np.polyfit(Vin[70:], Iout[70:], 1)
print(fit)
p = np.poly1d(fit)

plt.plot(Vin, Iout, '.', label="Experimental")
plt.plot(Vin[50:], p(Vin[50:]), '-', label="Theoretical (On-Region)")
plt.xlabel("Voltage (V)", fontsize=20)
plt.ylabel("Current (A)", fontsize=20)
plt.title("Applied Voltage vs. Measured Current ({} Resistor)".format(RES), fontsize=20)
plt.legend(loc=4, fontsize=18)

d = 1e6*fit
print(d)
plt.text(0.5, 0.000008, "Fit: ax + b\na = %.4f$\mu\mho$\nb = %.4f$\mu A$" % (d[0], d[1]), fontsize = 20)

plt.show()

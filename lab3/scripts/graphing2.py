import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

CUR_VOL = "data/experiment1_data2_2.csv"

with open(CUR_VOL, 'r') as f:
    reader = csv.reader(f)
    Vin = []
    Ibase = []
    Iemit = []
    for i, row in enumerate(reader):
        if i == 0: continue
        #if i < 135: continue
        #if i > 183: continue
        Vin.append(float(row[0]))
        Ibase.append(float(row[1]))
        Iemit.append(float(row[2]))

# Icollect = Ibase - Iemit
Icollect = []
for i in range(len(Ibase)):
    Icollect.append(Iemit[i] - Ibase[i])

# beta = Icollect / Ibase
beta = []
for i in range(len(Icollect)):
    beta.append(Icollect[i] / Ibase[i])
    
plt.semilogx(Ibase, beta, '.', label="Icollect vs. Ibase")
plt.title(r'$\beta$ vs. $I_{base}$', fontsize=20)
plt.ylim(180, 240)
plt.xlabel(r'$I_{base}$ (A)', fontsize=16)
plt.ylabel(r'$\beta$', fontsize=16)
plt.show()

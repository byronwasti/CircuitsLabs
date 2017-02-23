import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

VTC1 = "data/experiment3_1K_1.csv"
VTC2 = "data/experiment4_2K_1.csv"
VTC4 = "data/experiment4_4K_1.csv"
VTC6 = "data/experiment4_6K_1.csv"

Vin1  = []
Vout1 = []
Vin2  = []
Vout2 = []
Vin4  = []
Vout4 = []
Vin6  = []
Vout6 = []

with open(VTC1, 'r') as f:
    reader = csv.reader(f)

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 35 : continue
        if i > 245: continue
        Vin1.append(float(row[0]))
        Vout1.append(float(row[1]))


with open(VTC2, 'r') as f:
    reader = csv.reader(f)
    
    for i, row in enumerate(reader):
        if i == 0 : continue
        Vin2.append(float(row[0]))
        Vout2.append(float(row[1]))

with open(VTC4, 'r') as f:
    reader = csv.reader(f)
    
    for i, row in enumerate(reader):
        if i == 0 : continue
        Vin4.append(float(row[0]))
        Vout4.append(float(row[1]))

with open(VTC6, 'r') as f:
    reader = csv.reader(f)
    
    for i, row in enumerate(reader):
        if i == 0 : continue
        Vin6.append(float(row[0]))
        Vout6.append(float(row[1]))

fit2 = np.polyfit(Vin2[30:120], Vout2[30:120], 1)
poly2 = np.poly1d(fit2)
theoretical_VTC2 = lambda x: poly2(Vin2[30:120])

fit4 = np.polyfit(Vin4[30:85], Vout4[30:85], 1)
poly4 = np.poly1d(fit4)
theoretical_VTC4 = lambda x: poly4(Vin4[30:85])

fit6 = np.polyfit(Vin6[30:70], Vout6[30:70], 1)
poly6 = np.poly1d(fit6)
theoretical_VTC6 = lambda x: poly6(Vin6[30:70])

plt.plot(Vin2, Vout2, '.', label='VTC for inverter w/ $2K\Omega$ resistor')
plt.plot(Vin4, Vout4, '.', label='VTC for inverter w/ $4K\Omega$ resistor')
plt.plot(Vin6, Vout6, '.', label='VTC for inverter w/ $6K\Omega$ resistor')
# plt.plot(Vin1, Vout1, '.', label='VTC for follower w/ $1K\Omega$ resistor')
plt.plot(Vin2[30:120], theoretical_VTC2(Vin2[30:120]), label='theoretical VTC for inverter w/ $2K\Omega$ resistor')
plt.plot(Vin4[30:85], theoretical_VTC4(Vin4[30:85]), label='theoretical VTC for inverter w/ $4K\Omega$ resistor')
plt.plot(Vin6[30:70], theoretical_VTC6(Vin6[30:70]), label='theoretical VTC for inverter w/ $6K\Omega$ resistor')
plt.text(1, 4.5, '$V_{out}$ = %f$V_{in}$ + %fV' %(fit2[0], fit2[1]))
plt.text(1.2, 4.1, '$V_{out}$ = %f$V_{in}$ + %fV' %(fit4[0], fit4[1]))
plt.text(1.4, 3.7, '$V_{out}$ = %f$V_{in}$ + %fV' %(fit6[0], fit6[1]))
plt.title('$V_{out}$ vs. $V_{in}$', fontsize=20)
#plt.legend(fontsize=12, bbox_to_anchor=(0, 0), loc=2, borderaxespad=0.)
plt.legend()
plt.xlabel('$V_{in}$', fontsize=16)
plt.ylabel('$V_{out}$', fontsize=16)
plt.show()

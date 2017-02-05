import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from scipy.optimize import curve_fit

VOL_CUR = "data/e1_cur_2.csv"
CUR_VOL = "data/e1_vol_2.csv"

with open(VOL_CUR, 'r') as f:
    reader = csv.reader(f)
    Iin = []
    Vout = []
    for row in reader:
        Iin.append(float(row[0]))
        Vout.append(float(row[1]))

with open(CUR_VOL, 'r') as f:
    reader = csv.reader(f)
    Vin = []
    Iout = []
    for row in reader:
        Vin.append(float(row[0]))
        Iout.append(float(row[1]))

def func(x, a, b):
    return a * (np.exp(x/b) - 1)

#xdata= np.array([1, 8, 8, 21, 31, 42, 63, 64, 81, 110, 156, 211, 301, 336, 735])
#ydata = np.array([0.018, 0.0164, 0.0042, 0.0072, 0.0108, 0.0044, 0.0035, 0.0036, 0.0042, 0.0051, 0.0019, 0.0042, 0.0019, 8e-4, 2e-4])
xdata = np.array(Iin)
ydata = np.array(Vout)

#popt, pcov = curve_fit(func, Iin, Vout, p0=(1, 1e-6, 1))
popt, pcov = curve_fit(func, ydata, xdata, p0=(1e-13, 25e-3))
print(popt)
print(pcov)

y = [ func(i, *popt) for i in Vout]

plt.semilogy(Vout, Iin, '.', label="Sweep Current; Measure Voltage")
plt.semilogy(Vout, y, '-', label="Fit for Sweep Current; Measure Voltage")
plt.semilogy(Vin, Iout, '.', label="Sweep Voltage; Measure Current")
plt.axis([0.3, 0.7, 10e-10, 10e-3])
plt.xlabel("Voltage (V)", fontsize=20)
plt.ylabel("Current (A)", fontsize=20)
plt.title("Diode-Connected Transistor Characteristics", fontsize=20)
plt.text(0.35, 10e-5, "Fit: " + "$(%e) (e^{V/(%e)}-1)$" % (popt[0], popt[1]), fontsize=20)
plt.legend(loc=4, fontsize=20)
plt.show()

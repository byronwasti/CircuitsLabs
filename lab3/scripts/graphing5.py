import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME = "data/experiment2_1K_2.csv"
FILENAME2 = "data/experiment2_10K_2.csv"
FILENAME3 = "data/experiment2_100K_2.csv"
FILENAME4 = "data/experiment1_data2_1.csv"
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    vin_1k = []
    i_c_1k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        vin_1k.append(float(row[0]))
        i_c_1k.append(float(row[2]) - float(row[1]))

with open(FILENAME2, 'r') as f:
    reader = csv.reader(f)
    vin_10k = []
    i_c_10k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        vin_10k.append(float(row[0]))
        i_c_10k.append(float(row[2]) - float(row[1]))

with open(FILENAME3, 'r') as f:
    reader = csv.reader(f)
    vin_100k = []
    i_c_100k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        vin_100k.append(float(row[0]))
        i_c_100k.append(float(row[2]) - float(row[1]))

with open(FILENAME4, 'r') as f:
    reader = csv.reader(f)
    vin_n = []
    i_c_n = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        vin_n.append(float(row[0]))
        i_c_n.append(float(row[2]) - float(row[1]))

# I_c_n Fit
bounds = (100, 187)
vin_n_2 = vin_n[bounds[0]:bounds[1]]
i_c_n2 = i_c_n[bounds[0]:bounds[1]]
fit = np.polyfit(vin_n_2, np.log(i_c_n2), 1)
Is_2 = np.exp(fit[1])
UT_2 = 1/(fit[0])
fit_ = [ Is_2*np.exp(V/UT_2) for V in vin_n_2 ]

# Plotting
plt.semilogy(vin_1k, i_c_1k, '.', label="I_c 1K")
plt.semilogy(vin_10k, i_c_10k, '.', label="I_c 10K")
plt.semilogy(vin_100k, i_c_100k, '.', label="I_c 100K")
plt.semilogy(vin_n, i_c_n, '.', label="I_c No Resistor")
plt.semilogy(vin_n_2, fit_, '.', label="I_c No Resistor")

plt.text(1, 5e-3, "$I_c = I_se^{V_{be}/U_T}$\n$I_s$=%eA\n$U_T$=%eV" % (Is_2, UT_2))

plt.title("Voltage vs. Collector Current")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")

plt.legend()
plt.show()

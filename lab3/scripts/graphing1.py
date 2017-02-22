import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME = "data/experiment1_data2_2.csv"
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    x = []
    y1 = []
    y2 = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 50 : continue
        if i > 190 : continue
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[2]) - float(row[1]))


# I_b
fit1 = np.polyfit(x, np.log(y1), 1)
Is_1 = np.exp(fit1[1])
UT_1 = 1/(fit1[0])
print(Is_1, UT_1)
fit1_ = [ Is_1*np.exp(V/UT_1) for V in x ]

# I_c
x2 = x[45:150]
y2_ = y2[45:150]
fit2 = np.polyfit(x2, np.log(y2_), 1)
Is_2 = np.exp(fit2[1])
UT_2 = 1/(fit2[0])
print(Is_2, UT_2)
fit2_ = [ Is_2*np.exp(V/UT_2) for V in x2 ]

# Extracting \beta
beta = Is_2/Is_1
beta = (4e-3 - 1.9e-5)
Is_1_ = Is_1 * beta

# Plotting
plt.semilogy(x, y1, '.', label="I_b")
plt.semilogy(x, fit1_, '-', label="Fit I_b")

plt.semilogy(x, y2, '.', label="I_c")
plt.semilogy(x2, fit2_, '-', label="Fit I_c")

plt.text(0.5, 1e-3, "$I_c = I_se^{V_{be}/U_T}$\n$I_s$=%eA\n$U_T$=%eV" % (Is_2, UT_2) )

plt.text(0.65, 1e-7, "$I_b = (I_s/\\beta)e^{V_{be}/U_T}$\n$I_s$=%eA\n$U_T$=%eV\n$\\beta$=%e" % (Is_1_, UT_1, beta) )

plt.title("Voltage vs. Base Current and Collector Current")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.legend()
plt.show()

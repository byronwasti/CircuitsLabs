import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME = "data/experiment2_1K_1.csv"
FILENAME2 = "data/experiment2_10K_1.csv"
FILENAME3 = "data/experiment2_100K_1.csv"
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    vin_1k = []
    i_b_1k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        #if i < 30 : continue
        if i > 200 : continue
        vin_1k.append(float(row[0]))
        i_b_1k.append(float(row[1]))

    ib_1k_clean = []
    for i, _ in enumerate(i_b_1k):
        if i == 0: continue
        if i == (len(i_b_1k)-1): continue
        ib_1k_clean.append(i_b_1k[i-1] + i_b_1k[i] + i_b_1k[i+1])

with open(FILENAME2, 'r') as f:
    reader = csv.reader(f)
    vin_10k = []
    i_b_10k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 20 : continue
        vin_10k.append(float(row[0]))
        i_b_10k.append(float(row[1]))

    ib_10k_clean = []
    for i, _ in enumerate(i_b_10k):
        if i == 0: continue
        if i == (len(i_b_10k)-1): continue
        ib_10k_clean.append(i_b_10k[i-1] + i_b_10k[i] + i_b_10k[i+1])

with open(FILENAME3, 'r') as f:
    reader = csv.reader(f)
    vin_100k = []
    i_b_100k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        if i < 20 : continue
        vin_100k.append(float(row[0]))
        i_b_100k.append(float(row[1]))

    ib_100k_clean = []
    for i, _ in enumerate(i_b_100k):
        if i == 0: continue
        if i == (len(i_b_100k)-1): continue
        ib_100k_clean.append(i_b_100k[i-1] + i_b_100k[i] + i_b_100k[i+1])


# Finding shit
rb_1k = np.diff(vin_1k[1:-1])/np.diff(ib_1k_clean)
rb_10k = np.diff(vin_10k[1:-1])/np.diff(ib_10k_clean)
rb_100k = np.diff(vin_100k[1:-1])/np.diff(ib_100k_clean)
#rb_100k = np.diff(vin_100k)/np.diff(i_b_100k)


# Fit
beta = 60
UT = 6e-2
rb_fit_1k = lambda ib: beta*1e3*(1 + UT / (beta * ib * 1e3))
rb_fitted_1k = [ rb_fit_1k(ib) for ib in ib_1k_clean[:-1] ]

rb_fit_10k = lambda ib: beta*10e3*(1 + UT / (beta * ib * 10e3))
rb_fitted_10k = [ rb_fit_10k(ib) for ib in ib_10k_clean[:-1] ]

rb_fit_100k = lambda ib: beta*100e3*(1 + UT / (beta * ib * 100e3))
rb_fitted_100k = [ rb_fit_100k(ib) for ib in ib_100k_clean[:-1] ]

# Plotting
if False:
    plt.plot(vin_100k, i_b_100k)
    #plt.plot(np.diff(vin_1k))
    plt.xlabel("Voltage")
    plt.ylabel("Current")

if True:
    plt.loglog(ib_1k_clean[:-1], rb_1k, '.', label="1K")
    plt.loglog(ib_1k_clean[:-1], rb_fitted_1k, '-', label="1K Fit")

    plt.loglog(ib_10k_clean[:-1], rb_10k, '.', label="10K")
    plt.loglog(ib_10k_clean[:-1], rb_fitted_10k, '-', label="10K Fit")

    plt.loglog(ib_100k_clean[:-1], rb_100k, '.', label="100K")
    plt.loglog(ib_100k_clean[:-1], rb_fitted_100k, '-', label="100K Fit")

    plt.title("Incremental Resistance as a Function of Base Current")
    plt.xlabel("Current (A)")
    plt.ylabel("Incremental Resistance ($\Omega$)")

    plt.text(1.4e-6, 2.4e6, "Fit: $R_b = \\beta R (1 + U_T/(\\beta I_b R) )$  \n$\\beta$ = %e\n $U_T$ = %e\n $R \in [1K, 10K, 100K]$" % (beta, UT))

    plt.legend()

plt.show()

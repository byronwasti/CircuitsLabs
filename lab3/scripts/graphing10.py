import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME = "data/experiment2_1K_3.csv"
FILENAME2 = "data/experiment2_10K_1.csv"
FILENAME3 = "data/experiment2_100K_1.csv"
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    vin_1k = []
    i_c_1k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        #if i < 30 : continue
        #if i > 200 : continue
        vin_1k.append(float(row[0]))
        i_c_1k.append( float(row[2]) - float(row[1]) )

    ic_1k_clean = []
    for i, _ in enumerate(i_c_1k):
        if i == 0: continue
        if i == (len(i_c_1k)-1): continue
        ic_1k_clean.append(i_c_1k[i-1] + i_c_1k[i] + i_c_1k[i+1])
        
with open(FILENAME2, 'r') as f:
    reader = csv.reader(f)
    vin_10k = []
    i_c_10k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        #if i < 30 : continue
        #if i > 200 : continue
        vin_10k.append(float(row[0]))
        i_c_10k.append( float(row[2]) - float(row[1]) )

    ic_10k_clean = []
    for i, _ in enumerate(i_c_10k):
        if i == 0: continue
        if i == (len(i_c_10k)-1): continue
        ic_10k_clean.append(i_c_10k[i-1] + i_c_10k[i] + i_c_10k[i+1])

with open(FILENAME3, 'r') as f:
    reader = csv.reader(f)
    vin_100k = []
    i_c_100k = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        #if i < 30 : continue
        #if i > 200 : continue
        vin_100k.append(float(row[0]))
        i_c_100k.append( float(row[2]) - float(row[1]) )

    ic_100k_clean = []
    for i, _ in enumerate(i_c_100k):
        if i == 0: continue
        if i == (len(i_c_100k)-1): continue
        ic_100k_clean.append(i_c_100k[i-1] + i_c_100k[i] + i_c_100k[i+1])
    
    

# Finding shit
gm_1k = np.divide(np.diff(ic_1k_clean), np.diff(vin_1k[1:-1]))
gm_10k = np.divide(np.diff(ic_10k_clean), np.diff(vin_10k[1:-1]))
gm_100k = np.divide(np.diff(ic_100k_clean), np.diff(vin_100k[1:-1]))

# Fit Bullshit
alpha = 1

UT = 1.5e-2
RES = 0.35e3
gm_fit_1k = lambda ic: 1/RES * 1/(1 + UT /(ic*RES))
gm_fitted_1k = [ gm_fit_1k(ic) for ic in ic_1k_clean[:-1] ]

UT = 1.5e-2
RES2= 3.5e3
gm_fit_10k = lambda ic: alpha /RES2 * 1/(1 + alpha *UT /(ic*RES2))
gm_fitted_10k = [ gm_fit_10k(ic) for ic in ic_10k_clean[:-1] ]

UT = 1.5e-2
RES3= 35e3
gm_fit_100k = lambda ic: alpha /RES3 * 1/(1 + alpha *UT /(ic*RES3))
gm_fitted_100k = [ gm_fit_100k(ic) for ic in ic_100k_clean[:-1] ]

# Plotting
if False:
    plt.plot(vin_1k[1:-1], ic_1k_clean, '.')
    plt.plot(vin_10k[1:-1], ic_10k_clean, '.')
    #plt.plot(np.diff(vin_1k))
    #plt.plot(vin_1k[:-1], np.diff(i_b_1k))
    plt.xlabel("Voltage")
    plt.ylabel("Current")

if True:
    plt.loglog(ic_1k_clean[:-1], gm_1k, '.', label="1K")
    plt.loglog(ic_1k_clean[:-1], gm_fitted_1k, '-', label="1K Fit")

    plt.loglog(ic_10k_clean[:-1], gm_10k, '.', label="10k")
    plt.loglog(ic_10k_clean[:-1], gm_fitted_10k, '-', label="10k Fit")

    plt.loglog(ic_100k_clean[:-1], gm_100k, '.', label="100k")
    plt.loglog(ic_100k_clean[:-1], gm_fitted_100k, '-', label="100k Fit")

    plt.text(1e-7,1e-7, "Fit: $1/R * 1/ (1 + U_T / (I_c R))$ \n$U_T$ = %e\n$R \in [%e, %e, %e]$" % (UT, RES, RES2, RES3) )

    plt.title("Incremental Transductance Gain as a Function of Collector Current")
    plt.xlabel("Current (A)")
    plt.ylabel("Incremental Tranductance Gain ($\mho$)")
    plt.legend()

plt.show()

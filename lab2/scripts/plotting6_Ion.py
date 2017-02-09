import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

RESISTORS = [1e3, 10e3, 100e3]
V_ON = [0.584, 0.547, 0.553]
I_ON = [1.8203e-5, 3.1076e-6, 1.009e-6]
I_ON = [1e6*i for i in I_ON]

plt.semilogx(RESISTORS, I_ON, '.', markersize=20, label="Experimental")

plt.xlabel("Resistance Value ($\Omega$)", fontsize=20)
plt.ylabel("Current ($\mu$A)", fontsize=20)
plt.title("$I_{on}$ as a function of Resistance", fontsize=20)

plt.show()


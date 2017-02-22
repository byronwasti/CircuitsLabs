import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME = "data/experiment2_100K_2.csv"
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    vin = []
    i_c = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        vin.append(float(row[0]))
        i_c.append(float(row[2]) - float(row[1]))

# Fit
bounds = 40
fit = np.polyfit(vin[bounds:], i_c[bounds:], 1)
print(fit)
p = np.poly1d(fit)

# Plotting
plt.plot(vin, i_c, '.', label="I_c")
plt.plot(vin, p(vin), '-', label="I_c Fit")

plt.title("Collector Current as a Function of Base Voltage 100K Resistor")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.legend()

plt.text(3, 0.00001, "Fit: ax + b\na = %e$\mho$\nb=%eA" % (fit[0], fit[1]))

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = []
y = []
with open("../experiment4.csv", 'r') as f:
    for i,line in enumerate(f):
        if i == 0:
            continue

        line = line.strip()
        line = line.split(',')
        x.append(float(line[0]))
        y.append(float(line[1]))

sns.set_context(rc={'lines.markeredgewidth': 1})

f = lambda V, pos : V * 1/(2**(pos + 1) * 5e03)
theoretical1 = [ f(5, i) for i in x[:4] ]
theoretical2 = [ f(10, i) for i in x[4:] ]

print( x[:4], " and ", x[4:] )
plt.semilogy(x[:4], y[:4], 'x', label="5V Measurements")
plt.semilogy(x[4:], y[4:], 'x', label="10V Measurements")
plt.semilogy(x[:4], theoretical1, '-', label="5V Theoretical")
plt.semilogy(x[4:], theoretical2, '-', label="10V Theoretical")

plt.xlabel("Position", fontsize=18)
plt.ylabel("Current (A)", fontsize=18)
plt.title("Current Measurement in an R-2R Ladder Network", fontsize=18)
plt.legend()
plt.show()

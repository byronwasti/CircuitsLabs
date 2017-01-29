import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import smu

s = smu.smu()
s.set_function(1, 1) # SI/MV
s.set_function(2, 0) # SV/MI

Iin = np.linspace(-.0010, .0010, num=101)

Iout = []
for i in Iin:
    s.set_current(1, i)
    s.autorange(1)
    s.autorange(2)
    Iout.append(-s.get_current(2))

s.set_current(1, 0.)

fit = np.polyfit(Iin, Iout, 1)
print(fit)

p = np.poly1d(fit)

plt.plot(Iin, Iout, '.', Iin, p(Iin), '-')
plt.xlabel("Input Current (A)", fontsize=18)
plt.ylabel("Ouptut Current (A)", fontsize=18)
plt.title("Current Divider Ratio", fontsize=18)

plt.text(-0.0008, 0., "Divider Ratio: " + "{0:.6f}".format(fit[0]), fontsize=20)

plt.show()

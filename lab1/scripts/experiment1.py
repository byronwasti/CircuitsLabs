import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import smu

s = smu.smu()
vin = np.linspace(-2.0, 2.0, num=101)

Iout = []
for v in vin:
    s.set_voltage(1, v)
    s.autorange(1)
    Iout.append(s.get_current(1))
    
s.set_voltage(1, 0.)

fit = np.polyfit(vin, Iout, 1)
p = np.poly1d(fit)

res = fit[0]**(-1)

plt.plot(vin, Iout, '.', vin, p(vin), '-')
plt.xlabel("Voltage (V)", fontsize=18)
plt.ylabel("Current (A)", fontsize=18)
plt.title("Current Vs. Voltage for $665\Omega$", fontsize=18)
plt.text(-1, 0.001, "Resistance: " + "{0:.2f}".format(res) + "$\Omega$", fontsize=20)


plt.show()

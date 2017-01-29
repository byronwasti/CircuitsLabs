import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import smu

s = smu.smu()
vin = np.linspace(-2.0, 2.0, num=101)
s.set_current(2, 0.)

vout = []
for v in vin:
    s.set_voltage(1, v)
    s.autorange(1)
    s.autorange(2)
    vout.append(s.get_voltage(2))

s.set_voltage(1, 0.)

fit = np.polyfit(vin, vout, 1)
print(fit)
p = np.poly1d(fit)

plt.plot(vin, vout, '.', vin, p(vin), '-')
plt.xlabel("Input Voltage (V)", fontsize=18)
plt.ylabel("Ouptut Voltage (V)", fontsize=18)
plt.title("Voltage Divider Ratio", fontsize=18)

plt.text(-1, 0., "Divider Ratio: " + "{0:.6f}".format(fit[0]), fontsize=20)

plt.show()

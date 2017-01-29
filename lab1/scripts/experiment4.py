import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep

import smu

s = smu.smu()
s.set_function(1, 0) # SV/MI
s.set_function(2, 0) # SV/MI

s.set_voltage(1, 2) # 2 Volts on channel 1

while True:
    s.autorange(1)
    s.autorange(2)
    tmp = -s.get_current(2)
    print( "Current through Channel 2: " + str(tmp) )
    sleep(0.1)


#vin = np.linspace(-2, 2, num=101)

#iout = []
#for i in vin:
#    s.set_voltage(1, i)
#    s.autorange(1)
#    s.autorange(2)
#    iout.append(-s.get_current(2))

s.set_voltage(1, 0.)

#fit = np.polyfit(vin, iout, 1)
#print(fit)

#p = np.poly1d(fit)
#
#plt.plot(vin, iout, '.', vin, p(vin), '-')
#plt.xlabel("Input Voltage (V)", fontsize=18)
#plt.ylabel("Output Current (A)", fontsize=18)
#plt.title("Current Divider Ratio", fontsize=18)
#
#plt.show()

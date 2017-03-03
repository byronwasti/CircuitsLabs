import numpy as np
import smu
s = smu.smu()

s.set_current(1, 10e-6)
try:
    while True:
        s.get_current(
        pass
except KeyboardInterrupt:
    s.set_voltage(1, 0.)



import numpy as np
import smu
s = smu.smu()

s.set_voltage(1, 0.)
try:
    while True:
        cur = s.get_current(1)
        s.autorange(1)
        print(cur)
except KeyboardInterrupt:
    s.set_voltage(1, 0.)



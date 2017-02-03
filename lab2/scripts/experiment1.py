import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import smu

s = smu.smu()
TAKE_NEW_DATA = True

f = open("data_experiment1.csv", "wb")
writer = csv.writer(f)

if TAKE_NEW_DATA:
    pass


data = zip(x, y)
writer.writerows(data)
f.close()



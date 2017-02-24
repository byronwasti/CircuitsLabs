import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from time import sleep

FILE1 = "experiment1_Transistor1_1.csv"
FILE2 = "experiment1_Q1_1.csv"

with open(FILE1, 'r') as f:
    reader = csv.reader(f)
    x = []
    y1 = []
    y2 = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        x.append(row[0])
        y1.append(row[1])
        y2.append(row[2])

with open(FILE1, 'r') as f:
    reader = csv.reader(f)
    x2 = []
    y3 = []
    y4 = []

    for i, row in enumerate(reader):
        if i == 0 : continue
        x2.append(row[0])
        y3.append(row[1])
        y4.append(row[2])


plt.plot(x, y1, '.', label="i_b")
plt.plot(x2, y3, '-', label="i_e")

plt.figure()
plt.plot(x, y2, '.', label="i_b")
plt.plot(x2, y4, '-', label="i_e")

plt.show()

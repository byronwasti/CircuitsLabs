'''
Collector Current as a function of Base Voltage for all 4 Transistors
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

FILENAME1 = "../data/experiment1_Transistor1_1.csv"
FILENAME2 = "../data/experiment1_Transistor2_1.csv"
FILENAME3 = "../data/experiment1_Transistor3_1.csv"
FILENAME4 = "../data/experiment1_Transistor4_1.csv"
FILENAMES = [FILENAME1, FILENAME2, FILENAME3, FILENAME4]

DATAX =  [ [], [], [], [] ]
DATAY1 = [ [], [], [], [] ]
DATAY2 = [ [], [], [], [] ]

for j, FILENAME in enumerate(FILENAMES):

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        print(j)

        for i, row in enumerate(reader):
            if i == 0 : continue
            if float(row[0]) > 0.7 : continue
            if float(row[0]) < 0.4 : continue
            DATAX[j].append(float(row[0]))
            DATAY1[j].append(float(row[1]))
            DATAY2[j].append(float(row[2]) - float(row[1]))

fig, ax1 = plt.subplots()

for i in range(4):
    ax1.semilogy(DATAX[i], DATAY1[i], '.', label="Base Current Transistor %i" % i)

for i in range(4):
    ax1.semilogy(DATAX[i], DATAY2[i], '.', label="Collector Current Transistor %i" % i)


plt.xlabel("Base Voltage (V)")
plt.ylabel("Collector Current (A)")
plt.title("Collector Current vs. Base Voltage")
plt.legend()
plt.show()


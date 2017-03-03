
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

AVGX = []
AVGY1 = []
AVGY2 = []
for i in range(len(DATAX[0])):
    x = 0
    y1 = 0
    y2 = 0
    for j in range(4):
        x += DATAX[j][i]
        y1 += DATAY1[j][i]
        y2 += DATAY2[j][i]
        
    AVGX.append(x/4)
    AVGY1.append(y1/4)
    AVGY2.append(y2/4)

PER_DIFF_X = [ [], [], [], [] ]
PER_DIFF_Y1 = [ [], [], [], [] ]
PER_DIFF_Y2 = [ [], [], [], [] ]
for i in range(4):
    for j,x in enumerate(DATAX[i]):
        PER_DIFF_X[i].append( abs(AVGX[j] - x ) / AVGX[j] )
    for j,y in enumerate(DATAY1[i]):
        PER_DIFF_Y1[i].append( abs(AVGY1[j] - y ) / AVGY1[j] )
    for j,y in enumerate(DATAY2[i]):
        PER_DIFF_Y2[i].append( abs(AVGY2[j] - y ) / AVGY2[j] )


#for i in range(4):
    #plt.semilogy(DATAX[i], DATAY1[i], '.', label="Transistor %i" % i)
#plt.semilogy(AVGX, AVGY1, '.', label="Transistor AVG")

for i in range(4):
    plt.plot(AVGX, PER_DIFF_Y1[i], '.', label="Transistor %i" % i)

plt.xlabel("Base Voltage (V)")
plt.ylabel("Percent Difference from Mean")
plt.title("Percent Difference from Mean Value as a Function of Base Voltage")
plt.legend()
plt.show()


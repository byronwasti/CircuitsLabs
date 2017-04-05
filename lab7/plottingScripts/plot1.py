import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def plot_exp1_cv(FILENAME, label):
    i_x = []
    i_y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_x.append(float(row[0]))
            i_y.append(float(row[1]))
    
    plt.plot(i_x, i_y, '.', label=label)


def plot_exp1_cv_ImI(FILENAME1, FILENAME2, label):
    i_x = []
    i_y1 = []
    i_y2 = []
    i_y = []

    with open(FILENAME1, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_x.append(float(row[0]))
            i_y1.append(float(row[1]))
    
    with open(FILENAME2, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_y2.append(float(row[1]))
    
    i_y = np.subtract(i_y1, i_y2)
    
    plt.plot(i_x, i_y, '.', label=label)

def plot_exp1_cv_IpI(FILENAME1, FILENAME2, label):
    i_x = []
    i_y1 = []
    i_y2 = []
    i_y = []

    with open(FILENAME1, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_x.append(float(row[0]))
            i_y1.append(float(row[1]))
    
    with open(FILENAME2, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_y2.append(float(row[1]))
    
    i_y = np.add(i_y1, i_y2)
    
    plt.plot(i_x, i_y, '.', label=label)

if __name__ == "__main__":
    FILENAME1 = "../data/weak_V2-3V_I1_1.csv"
    FILENAME2 = "../data/weak_V2-3V_I2_2.csv"
    FILENAME3 = "../data/weak_V2-3V_V_1.csv"
    FILENAME4 = "../data/weak_V2-3.5V_I1_1.csv"
    FILENAME5 = "../data/weak_V2-3.5V_I2_2.csv"
    FILENAME6 = "../data/weak_V2-3.5V_V_1.csv"
    FILENAME7 = "../data/weak_V2-4V_I1_1.csv"
    FILENAME8 = "../data/weak_V2-4V_I2_2.csv"
    FILENAME9 = "../data/weak_V2-4V_V_1.csv"

    plot_exp1_cv(FILENAME1, "$V_2$ = 3V, $I_1$")
    plot_exp1_cv(FILENAME4, "$V_2$ = 3.5V, $I_1$")
    plot_exp1_cv(FILENAME7, "$V_2$ = 4V, $I_1$")

    plot_exp1_cv(FILENAME2, "$V_2$ = 3V, $I_2$")
    plot_exp1_cv(FILENAME5, "$V_2$ = 3.5V, $I_2$")
    plot_exp1_cv(FILENAME8, "$V_2$ = 4V, $I_2$")

    plot_exp1_cv_ImI(FILENAME1, FILENAME2, "$V_2$ = 3V, $I_1 - I_2$")    
    plot_exp1_cv_ImI(FILENAME4, FILENAME5, "$V_2$ = 3.5V, $I_1 - I_2$")    
    plot_exp1_cv_ImI(FILENAME7, FILENAME8, "$V_2$ = 4V, $I_1 - I_2$")    

    plot_exp1_cv_IpI(FILENAME1, FILENAME2, "$V_2$ = 3V, $I_1 + I_2$")    
    plot_exp1_cv_IpI(FILENAME4, FILENAME5, "$V_2$ = 3.5V, $I_1 + I_2$")    
    plot_exp1_cv_IpI(FILENAME7, FILENAME8, "$V_2$ = 4V, $I_1 + I_2$")    
 
    plt.xlabel("$V_1 - V_2$ (V)", fontsize=16)
    plt.ylabel("Current (A)", fontsize=16)
    plt.title("$I_1$, $I_2$, $I_1 - I_2$, and $I_1 + I_2$ vs. $V_1 - V_2$", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

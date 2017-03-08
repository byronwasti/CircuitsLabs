import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def plot_IvI(FILENAME, label):
    i_x = []
    i_y = []

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0 : continue
            i_x.append(float(row[0]))
            i_y.append(-float(row[1]))

    log_i_x = np.log(i_x[100:300])
    log_i_y = np.log(i_y[100:300])

    fit = np.polyfit(log_i_x, log_i_y, 1)
    theoretical = np.power(i_x, fit[0]) * np.exp(fit[1])

    plt.loglog(i_x, i_y, '.', label=label)
    plt.loglog(i_x, theoretical, label=label+" Theoretical")

    return fit

if __name__ == "__main__":
    fit1 = plot_IvI("../data/experiment2_y_2K_1.csv", "$2K\Omega$")
    fit2 = plot_IvI("../data/experiment2_y_20K_1.csv", "$20K\Omega$")
    fit3 = plot_IvI("../data/experiment2_y_200K_2.csv", "$200K\Omega$")

    plt.text(1.5e-8, 5e-6, '$I_z$ = $I_y^\\alpha$ * $\\beta$\n$\\beta$ = $\\sqrt{I_x}$\n$\\alpha = %f$, $\\beta = %fA$\n$\\alpha = %f$, $\\beta = %fA$\n$\\alpha = %f$, $\\beta = %fA$' %(fit1[0], np.exp(fit1[1]), fit2[0], np.exp(fit2[1]), fit3[0], np.exp(fit3[1])), fontsize=16)

    plt.xlabel("$I_y$ (A)", fontsize=16)
    plt.ylabel("$I_z$ (A)", fontsize=16)
    plt.title("$I_z$ vs. $I_y$", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

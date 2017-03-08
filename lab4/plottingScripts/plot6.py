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
            i_x.append(-float(row[0]))
            i_y.append(-float(row[1]))

    log_i_x = np.log(i_x[150:300])
    log_i_y = np.log(i_y[150:300])

    fit = np.polyfit(log_i_x, log_i_y, 1)
    theoretical = np.power(i_x, fit[0]) * np.exp(fit[1])

    plt.loglog(i_x, i_y, '.', label=label)
    plt.loglog(i_x, theoretical, label=label+" Theoretical")

    return fit

if __name__ == "__main__":
    fit1 = plot_IvI("../data/experiment3_x_2K_1.csv", "$2K\Omega$")
    fit2 = plot_IvI("../data/experiment3_x_20K_1.csv", "$20K\Omega$")
    fit3 = plot_IvI("../data/experiment3_x_200K_1.csv", "$200K\Omega$")

    plt.text(1.5e-8, 1.5e-6, '$I_z$ = $\\beta$$I_y^\\alpha$\n$\\beta$ = $I_x^2$\n$\\alpha = %f$, $\\beta = %eA^2$\n$\\alpha = %f$, $\\beta = %eA^2$\n$\\alpha = %f$, $\\beta = %eA^2$' %(fit1[0], np.exp(fit1[1]), fit2[0], np.exp(fit2[1]), fit3[0], np.exp(fit3[1])), fontsize=16)
    # plt.text(1e-8, 3.5e-5, '$I_z$ = $I_x$^%f + %fA' %(fit1[0], fit1[1]))

    plt.xlabel("$I_x$ (A)", fontsize=16)
    plt.ylabel("$I_z$ (A)", fontsize=16)
    plt.title("$I_z$ vs. $I_x$", fontsize=20)
    plt.legend(fontsize=12, loc='best')
    plt.show()

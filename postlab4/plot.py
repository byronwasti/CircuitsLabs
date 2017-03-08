import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def parseData(Filename):
    data = {}
    vals = []
    vy = None
    with open(Filename, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0: continue  # Skip first
            if row[0].startswith("Step"): # Get setup
                new = row[0].split("=")[1].split(" ")[0]
                print(row)
                print(new)
                vy = float(new)
                data[vy] = [ [], [] ]
                vals.append(vy)
            else:
                data[vy][0].append( float(row[0]) )
                data[vy][1].append( float(row[3]) )
                

    return data, vals


if __name__ == "__main__":
    #data, vals = parseData("FinalSim.csv")
    data, vals = parseData("./Simulation/data.txt")
    
    for i in vals[::-1]:
        plt.plot(data[i][0], data[i][1], 'x', mew=1, label="$V_y$ = %f" % i)
        plt.plot(data[i][0], (lambda x: np.sqrt( np.square(x) + i**2))(data[i][0]), '-')

    plt.legend()
    plt.title("Pythagorator Theoritical vs. Simulation")
    plt.xlabel("$V_x$ (V)")
    plt.ylabel("$V_z$ (V)")
    plt.show()


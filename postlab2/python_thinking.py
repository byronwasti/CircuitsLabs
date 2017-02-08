import numpy as np

V2 = 1
U_T = 23e-3
V1 = 100

V = V1 - U_T* np.log(1 + np.exp( (V1 - V2) / U_T ) )

print(V)

import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
# Variables 
S0 = 995 
I0 = 5
R0 = 0
N = S0 + I0 + R0
a = 0.0005
b = 1 / 7 
T = 40 
t = np.ndarray(T)
for x in range(0, t.shape[0]):
    t[x] = x


#print(t)



def SIR(S0, I0, R0, a, b, T=100):
    t = np.ndarray(T)
    for x in range(0, t.shape[0]):
        t[x] = x
    S = np.ndarray(T)
    I = np.ndarray(T)
    R = np.ndarray(T)
    for n in range(0,t.shape[0]):
        S = np.append(S, [S0 - a * (S0 * I0) ])
        I = np.append(I, [I0 + a * (S0 * I0) - b * I0]) 
        R = np.append(R, [R0 + b * I0])
        S0 = S[-1]
        I0 = I[-1]
        R0 = R[-1]
    print(S)
    return S, I, R, t   
    

def plotting(t, S, I, R):
    fig, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot(t, S, 'blue')
    ax.plot(t, I, 'orange')
    ax.plot(t, R, 'green')
    plt.show()

S, I, R, t = SIR(S0,I0,R0, a, b, T=50)
plotting(t, S, I, R )

    
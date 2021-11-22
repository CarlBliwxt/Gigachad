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


def SIR(S0, I0, R0, a, b, T=100):
    t = np.linspace(0,T-1, T)
    S = []
    I = []
    R = []
    for n in range(T):
        S.append(S0 - a * (S0 * I0)) 
        I.append(I0 + a * (S0 * I0) - b * I0) 
        R.append(R0 + b * I0)
        print(S)
        S0 = S[n]
        I0 = I[n]
        R0 = R[n]
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

    
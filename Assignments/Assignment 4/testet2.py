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
    t = np.ndarray(T+1)
    for x in range(T+1):
        t[x] = x

    S = np.ndarray(T)
    I = np.ndarray(T)
    R = np.ndarray(T)
    S_temp = S0
    I_temp = I0
    R_temp = R0
    for n in range(0, T):
        S = np.append(S_temp, S0 - a * (S0 * I0) )
        I = np.append(I_temp, I0 + a * (S0 * I0) - b * I0) 
        R = np.append(R_temp, R0 + b * I0)
        S_temp = S
        I_temp = I
        R_temp = R
        S0 = S[-1]
        I0 = I[-1]
        R0 = R[-1]
    return S, I, R, t   
    

def plotting(t, S, I, R):
    fig, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot(t, S, 'blue', alpha=0.7, linewidth=2, label='Susceptible')
    ax.plot(t, I, 'orange',  alpha=0.7, linewidth=2, label='Infected')
    ax.plot(t, R, 'green', alpha=0.7, linewidth=2, label='Recovered')
    ax.set_xlabel('Time (weeks)')
    ax.set_ylabel('Number of individuals')
    
    legend = ax.legend()
    legend.get_frame().set_alpha(1)
    plt.show();

S, I, R, t = SIR(S0,I0,R0, a, b, T=50)
plotting(t, S, I, R )

    
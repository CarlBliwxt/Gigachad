import numpy as np
import matplotlib.pyplot as plt 
# Variables 
S0 = 995 
I0 = 5
R0 = 0
N = S0 + I0 + R0
a = 0.0005
b = 1 / 7 
T = 40 


def SIR(S0, I0, R0, a, b, T=100):
    # Allocationg of, t, on element bigger than T because indexing starts at 0 
    t = np.ndarray(T + 1)
    for x in range(T + 1):
        t[x] = x
    # Allocating the variables 
    S = np.ndarray(T)
    I = np.ndarray(T)
    R = np.ndarray(T)
    # updating the variables 
    S_temp = S0
    I_temp = I0
    R_temp = R0
    for n in range(T): # Iterate over the entire time period 
        S = np.append(S_temp, [S0 - a * (S0 * I0)] )
        I = np.append(I_temp, [I0 + a * (S0 * I0) - b * I0]) 
        R = np.append(R_temp, [R0 + b * I0])
        # Updates the every temp to the new array
        S_temp = S
        I_temp = I
        R_temp = R
        # Takes the most recent value and sets this as the new S0. 
        S0 = S[-1]
        I0 = I[-1]
        R0 = R[-1]
    return S, I, R, t   
    
def plotting(t, S, I, R, d):
    fig, ax = plt.subplots(2)
    # Plots 
    ax[0].plot(t, S, 'blue', linewidth = 4, label='Susceptible')
    ax[0].plot(t, I, 'orange', linewidth = 4, label='Infected')
    ax[0].plot(t, R, 'green',  linewidth = 4, label='Recovered')
    ax[1]. plot(t, d, "red", alpha=1, linewidth=4, label='death toll')
    # Labels for plots
    ax[0].set_ylabel('Number of individuals')
    ax[1].set_ylabel('Number of individuals')
    ax[1].set_xlabel('Time (weeks)')

    # Setting legends for both grafs
    legend1 = ax[0].legend()
    legend1.get_frame().set_alpha(1)
    legend2 = ax[1].legend()
    legend2.get_frame().set_alpha(1)

    plt.show();

# Getting the variables for the plots 
S, I, R, t = SIR(S0, I0 , R0, a, b, T=50)
d = np.diff(R) * 0.9
d = np.append(d, [0] )
plotting(t, S, I, R, d)
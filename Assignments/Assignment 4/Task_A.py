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
    t, S, I, R = np.zeros(T+1), np.zeros(T+1), np.zeros(T+1), np.zeros(T+1)

    #Updating first values 
    S[0], I[0], R[0], t[0] = S0, I0, R0, 0
    for n in range(1, T+1): # Iterate over the entire time period 
        S[n] = S[n-1] - a * (S[n-1] * I[n-1])
        I[n] = I[n-1] + a * (S[n-1] * I[n-1]) - b * I[n-1]
        R[n] = R[n-1] + b * I[n-1]
        t[n] = n
        # Takes the most recent value and sets this as the new S0. 
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
d = np.append(d, 0)

plotting(t, S, I, R, d)
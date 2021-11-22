from numpy import random
import matplotlib as m
from matplotlib import colors
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt 

#Constants defining state of the individuals in the model
SUSCEPTIBLE=0
INFECTED=1
RECOVERED=2
NON_HUMAN=3

#Returns a colormap that can be used to plot the results.
def SIRcmap():
    colors_list=['#f2f2f2', '#e41a1c', '#377eb8', '#104c6d']
    mp_SIR= m.colors.LinearSegmentedColormap.from_list('SIR_cmap', colors_list)
    return mp_SIR

def createSIR2D(rows, columns):
    grid = np.zeros((rows, columns))
    return grid

def findNeighbors(grid, i, j):
    neighs = []
    if (i + j >= 1  and i >= 0 and i <= len(grid) and j >= 0 and j <= len(grid[0])): # Restricting so it founds in pounds
        if (i + 1 < len(grid) and grid[i+1, j] == SUSCEPTIBLE):
            neighs.append((i+1, j ))
        if ( i-1 >= 0 and grid[i-1, j] == SUSCEPTIBLE):
            neighs.append((i-1, j)) 
        if (j-1 >= 0 and grid[i, j-1] == SUSCEPTIBLE):
            neighs.append((i, j-1))
        if (j+1 < len(grid[0]) and grid[i, j+1] == SUSCEPTIBLE):
            neighs.append((i, j+1))

    return neighs

def infect(grid, i, j, alpha):
    probablity = np.random.rand() # random between 0 and 1
    if (grid[i, j] == INFECTED):  # Check if it is already infected,
        infected = True
    elif (grid[i, j] == SUSCEPTIBLE):  # check if person is Suspceptible
        if (probablity < alpha): # If alpha is bigger than prob, infect
            infected = True
        else: 
            infected = False
    else: 
        infected = False
    return infected

def recover(grid, i, j, beta):
    probability = np.random.rand() # random generator between 0 and 1
    
    if (grid[i, j] == INFECTED):  # Checks if the person is infeced
        if (probability < beta):
            recovered = True
        else: 
            recovered = False
    return recovered

def plot2D_SIR(grid, title='SIR model'):
    custom_lines = [Line2D([0], [0], color="#f2f2f2", lw=2), # Use of Line2D to get the right legend
                    Line2D([0], [0], color="#e41a1c", lw=2),
                    Line2D([0], [0], color="#377eb8", lw=2),
                    Line2D([0], [0], color="#104c6d", lw=2),
                    ]
    fig, ax = plt.subplots()
    names = ["SUSCEPTIBLE" ,"INFECTED ", "RECOVERED", "NON_HUMAN" ] # Names for legend
    fig = ax.imshow(grid, SIRcmap()) 
    ax.legend(custom_lines, names)
    ax.set_title(title)
    plt.show()
    return

def time_step(current_grid, alpha, beta): 
    temp =[]
    new_grid = current_grid.copy() # Copying the input to new_grid
   # Nestled for loop, to go over rows and columns in the input grid
    for i in range(len(current_grid)):
        for j in range(len(current_grid[0])):
            if current_grid[i][j] == INFECTED : # Check if they are infecteded
                temp.append((i, j)) # append the coordinates to a temp 
    
    # To handle the infected function
    for x in range(len(temp)): # for loop to find neigbors
        pos_i = temp[x][0] # Take out pos i, in the vector
        pos_j = temp[x][1] # Only two dimensional so only need [0] and [1]
        a = findNeighbors(current_grid, pos_i, pos_j) # 
        for y in range(len(a)): # Take out coordinates of findNeighbors function
            i = a[y][0]
            j = a[y][1]
            if (infect(current_grid, i, j, alpha) == True) : # If infect returns true, add infected at coordinate
                new_grid[i, j ] = INFECTED
    # To handle the recover function, 
    #Nestled for loop, to loop over every element in c
    for a in range(len(new_grid)): #
        for b in range(len(new_grid[0])):
            if (new_grid[a, b] == INFECTED and recover(new_grid, a, b, beta) == True):
                new_grid[a, b] = RECOVERED

    return new_grid


def plotting(t, S, I, R, d):
    fig, ax = plt.subplots(2)
    ax[0].plot(t, S, 'blue', alpha=0.7, linewidth=2, label='Susceptible')
    ax[0].plot(t, I, 'orange',  alpha=0.7, linewidth=2, label='Infected')
    ax[0].plot(t, R, 'green', alpha=0.7, linewidth=2, label='Recovered')

    ax[0].set_ylabel('Number of individuals')
    ax[1].set_xlabel('Time (weeks)')
    ax[1]. plot(t, d, "red", alpha=0.7, linewidth=2, label='death toll')
    
    legend1 = ax[0].legend()
    legend1.get_frame().set_alpha(1)
    legend2 = ax[1].legend()
    legend2.get_frame().set_alpha(1)
    plt.show();

#Settings for 2D
T = 50
alpha = 0.9
beta = 0.15
amount_INFECTED = 100
grid = np.loadtxt('worldmap.dat', dtype=int, delimiter=',')
amount = 0
while amount < amount_INFECTED:
    x = random.randint(len(grid))
    y = random.randint(len(grid[0]))
    if grid[x,y] == SUSCEPTIBLE:
        grid[x, y ] = INFECTED
        amount += 1


grids =[]
grids.append(grid)

# Variables 

S = np.ndarray(T) # allocated
I = np.ndarray(T)
R = np.ndarray(T)
S0 = np.sum( grid == SUSCEPTIBLE)
I0 = np.sum( grid == INFECTED)
R0 = np.sum( grid == RECOVERED)
t = np.ndarray(T+1)
for x in range(T+1):
    t[x] = x
# Run the simulation
for n in range(0, T):
    grid = time_step(grid, alpha, beta)
    S = np.append(S0, np.sum( grid == SUSCEPTIBLE))
    S0 = S
    I = np.append(I0, np.sum( grid == INFECTED))
    I0 = I
    R = np.append(R0, np.sum( grid == RECOVERED))
    R0 = R
    grids.append(grid)



[plot2D_SIR(grids[t], title=f'week {t}') for t in np.arange(0,T+1,T//5)]
d = np.diff(R) * 0.9
d = np.append(d, [0] )
plotting(t, S, I, R, d)


    

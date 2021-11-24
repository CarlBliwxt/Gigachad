from matplotlib.text import Text
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
     # The first if, states which boundary conditions for i and j that needs to be fufilled
    # To be inside the the grid, 
    # The next four if exists to find the actual neighbors
    # It checks if it is outside the grid or not and if the point is equal to zero  
    if (i + j >= 1  and i >= 0 and i <= len(grid) and j >= 0 and j <= len(grid[0])): 
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
    elif (grid[i, j] == SUSCEPTIBLE and probablity < alpha):  # check if person is Suspceptible
        infected = True
    else: 
        infected = False
    return infected

def recover(grid, i, j, beta):
    probability = np.random.rand() # random generator between 0 and 1
    if (grid[i, j] == INFECTED and probability < beta):  # Checks if the person is infeced
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
    fig = ax.imshow(grid, cmap=SIRcmap()) 
    ax.legend(custom_lines, names)
    ax.set_title(title)
    plt.show()
    return

def time_step(current_grid, alpha, beta): 
    infected_position =[]
    new_grid = current_grid.copy() # Copying the input to new_grid
   # Nestled for loop, to go over rows and columns in the input grid
    for i in range(len(current_grid)):
        for j in range(len(current_grid[0])):
            if current_grid[i][j] == INFECTED : # Check if they are infecteded
                infected_position.append((i, j)) # append the coordinates to a temp 
    
    # To handle the infected function
    for x in range(len(infected_position)): # for loop to find neigbors
        pos_i = infected_position[x][0] # Take out pos i, in the vector
        pos_j = infected_position[x][1] # Only two dimensional so only need [0] and [1]
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
    # Plots 
    ax[0].plot(t, S, 'blue', linewidth = 2, label='Susceptible')
    ax[0].plot(t, I, 'orange', linewidth = 2, label='Infected')
    ax[0].plot(t, R, 'green',  linewidth = 2, label='Recovered')
    ax[1]. plot(t, d, "red", linewidth = 2, label='Death toll')
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


#Settings and variables 
T = 50
alpha = 0.9
beta = 0.15
amount_INFECTED = 100
# Loading in the grid 
grid = np.loadtxt('worldmap.dat', dtype=int, delimiter=',')
amount = 0 # Set it to zero for the while loop

# We do a while loop to get 100 infected
while amount <= amount_INFECTED:
    x = random.randint(len(grid)) # Generate a number between 0 and max value of rows
    y = random.randint(len(grid[0])) # Generate a number between 0 and max value of columns 
    if grid[x,y] == SUSCEPTIBLE: # Checks if the given coordinate is a zero 
        grid[x, y ] = INFECTED
        amount += 1

# Storing grids 
grids =[]
grids.append(grid)

# Variables 
#Allocation for the arrays
t = np.ndarray(T)
for x in range(T):
    t[x] = x
S = np.ndarray(T) 
I = np.ndarray(T)
R = np.ndarray(T)
# Setting inital values when starting
S0 = np.sum( grid == SUSCEPTIBLE)
I0 = np.sum( grid == INFECTED)
R0 = np.sum( grid == RECOVERED)
# For the 1D-simulation 
    # Summing all variables and adding it to the arrays 

# Running the simulation 
for n in range(0, T):
    # For the 2D-simulation 
    grid = time_step(grid, alpha, beta)
    S[n]= np.sum(grid == SUSCEPTIBLE)
    I[n] = np.sum(grid == INFECTED)
    R[n]= np.sum(grid == RECOVERED)
    grids.append(grid)

# Calculation of deathtolls
d = np.diff(R) * 0.9
d = np.append(d, [0] )   
# Plot for 2D
[plot2D_SIR(grids[t], title=f'week {t}') for t in np.arange(0,T+1,T//5)]
#plot for 1D 
plotting(t, S, I, R, d)


    

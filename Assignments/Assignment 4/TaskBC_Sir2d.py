import matplotlib as m
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

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
    if (grid[i, j] == INFECTED):  # Check if it is al   ready infected,
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
    
    fig = ax.imshow(grid, cmap = SIRcmap(), vmax = NON_HUMAN, vmin = SUSCEPTIBLE)
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

# Settings
T = 50
M = 8
N = 6
alpha = 0.6
beta = 0.05

# Initialize the grid and variable grids
grid = createSIR2D(rows=M, columns=N)
grid[1, 0] = INFECTED
grids = []
grids.append(grid)

# Run the simulation
for n in range(T):
    grid = time_step(grid, alpha, beta)
    print(grid)
    grids.append(grid)

[plot2D_SIR(grids[t], title=f'week {t}') for t in np.arange(0,T+1,T//5)]
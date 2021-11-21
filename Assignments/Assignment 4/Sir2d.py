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
    mp_SIR=m.colors.LinearSegmentedColormap.from_list('SIR_cmap', colors_list)

    return mp_SIR

def createSIR2D(rows, columns):
    grid = np.zeros((rows, columns))
    return grid

def findNeighbors(grid, i, j):
    neighs = []
    if (i + j > 1  and i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])):
        if (i + 1 < len(grid) and grid[i+1, j] == 0):
            neighs.append((i+1, j ))
        if ( i-1 >= 0 and grid[i-1, j] == 0):
            neighs.append((i-1, j)) 
        if (j-1 >= 0 and grid[i, j-1] == 0):
            neighs.append((i, j-1))
        if (j+1 < len(grid[0]) and grid[i, j+1] == 0):
            neighs.append((i, j+1))

    return neighs

def infect(grid, i, j, alpha):
    probablity = np.random.rand()
    if (grid[i, j] == 1): 
        infected = True
    elif (grid[i, j] == 0): 
        if (probablity < alpha):
            infected = True
        else: 
            infected = False
    else: 
        infected = False

    return infected

def recover(grid, i, j, beta):
    probability = np.random.rand()
    
    if (grid[i, j] == 1): 
        if (probability < beta):
            recovered = True
        else: 
            recovered = False
    return recovered

def plot2D_SIR(grid, title='SIR model'):
    custom_lines = [Line2D([0], [0], color="#f2f2f2", lw=4),
                    Line2D([0], [0], color="#e41a1c", lw=4),
                    Line2D([0], [0], color="#377eb8", lw=4),
                    Line2D([0], [0], color="#104c6d", lw=4),
                    ]
    fig, ax = plt.subplots()
    names = ["SUSCEPTIBLE" ,"INFECTED ", "RECOVERED", "NON_HUMAN" ]
    im = ax.imshow(grid, SIRcmap())
    ax.legend(custom_lines, names)
    plt.show()
    #Implement this function yourself
    return

def time_step(current_grid, alpha, beta): 
    temp =[]
    new_grid = current_grid.copy()
    for i in range(len(current_grid)):
        for j in range(len(current_grid[0])):
            if current_grid[i][j] == 1 :
                temp.append((i, j))
    for x in range(len(temp)): 
        pos_i = temp[x][0]
        pos_j = temp[x][1]
        a = findNeighbors(current_grid, pos_i, pos_j)
        for y in range(len(a)):
            i = a[y][0]
            j = a[y][1]
            if (infect(current_grid, i, j, alpha) == True) :
                new_grid[i, j ] = INFECTED

    for a in range(len(new_grid)):
        for b in range(len(current_grid[0])):
            if (new_grid[a][b] == 1 and recover(new_grid, a, b, beta) == True):
                new_grid[a, b] = RECOVERED

    return new_grid

grid = createSIR2D(rows=8, columns=6)
grid[4, 3] = INFECTED
grids =[]
grids.append(grid)

T = 50
alpha = 0.2 
beta = 0.15
# Run the simulation
for n in range(T):
    grid = time_step(grid, alpha, beta)
    print(grid)
    grids.append(grid)

 #Plot the results
#[plot2D_SIR(grids[t], title=f'week {t}') for t in np.arange(0,T+1,T//5)]








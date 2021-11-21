import numpy as np
import matplotlib.pyplot as plt 

#Constants defining state of the individuals in the model
SUSCEPTIBLE=0
INFECTED=1
RECOVERED=2
NON_HUMAN=3

def createSIR2D(rows, columns):
    grid = np.zeros((rows, columns))
    return grid

def findNeighbors(grid, i, j):
    neighs = grid
    x = int(i)
    y = int(j)
    for i in range(-1, 2):
        for y in range(-1, 2):
            neighs[i-1][j]
            neighs[i+1][j]
            neighs[i][j-1]
            neighs[i][j+1]
    return neighs

        


grid = createSIR2D(rows=8, columns=6)
grid[4, 3] = INFECTED
grid[3, 3] = RECOVERED
#print(grid)
a = findNeighbors(grid, 4,3)
print(a)

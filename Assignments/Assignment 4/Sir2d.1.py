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
    neighs = []

    if (i + j > 1  and i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])):
        if (grid[i][j] == 0 
            if (i + 1 < len(grid) and i-1 > 0 and j-1 > 0 and j+1 < len(grid[0]) ):
                neighs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
    return neighs

def infect(grid, i, j, alpha):
    """ Determines if an individual at position (i, j) is going to be infected during the current week.

    Parameters
    ----------
    grid : 2D numpy.ndarray
        Input grid on which to work.
    i : integer
        Row index of the individual.
    j : integer
        Column index of the individual.
    alpha : float
        Model parameter giving the probability to get infected in a certain week.

    Returns
    -------
    infected : boolean
        Set to True if the individual at position (i, j) will be infected in current week. Otherwise False.
    """
    #Implement this function yourself
    #Delete the following line. Variables are set to None so that you can use
    #the module even if the function body is not defined.
    infected=None
    return infected


grid = createSIR2D(rows=8, columns=6)
print(len(grid[0]))
grid[4, 3] = INFECTED
grid[3, 3] = RECOVERED
print(grid)
a = findNeighbors(grid, 4 ,5)
print(a)


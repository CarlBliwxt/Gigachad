#Module implementing functions to work with SIR model.
import matplotlib as m
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


def SIR(S0, I0, R0, a, b, T=100):
    """Runs SIR model for T steps.

    Parameters
    ----------
    S0 : integer
        initial size of susceptible population
    I0 : integer
        initial size of infected population
    R0 : integer
        initial size of recovered population
    a : float
        rate of spread of infection
    b : float
        rate of recovery
    T : integer
        total number of weeks in simulation

    Returns
    -------
    S : numpy array
        array of size T, containing the size of susceptible population
    I : numpy array
        array of size T, containing the size of infected population
    R : numpy array
        array of size T, containing the size of recovered population
    t : numpy array
        array of size T, containing the time intervals
    """

    #Implement this function yourself
    #Delete the following line. Variables are set to None so that you can use
    #the module even if the function body is not defined.
    S, I, R, t = None
    return S, I, R, t

def createSIR2D(rows, columns):
    """ Creates 2D grid to run the 2D SIR model on.

    Parameters
    ----------
    rows : integer
        number of rows in the grid
    columns : integer
        number of columns in the grid
    
    Returns
    -------
    grid : 2D numpy.ndarray of integers
        2D grid where all individuals are set to SUSCEPTIBLE
    """
    #Implement this function yourself
    #Delete the following line. Variables are set to None so that you can use
    #the module even if the function body is not defined.
    grid=None
    return grid

def findNeighbors(grid, i, j):
    """ Find indices of neighbours of the individual at position (i, j) in grid.

    Parameters
    ----------
    grid : 2D numpy.ndarray
        Input grid on which to work.
    i : integer
        Row index of the individual.
    j : integer
        Column index of the individual.

    Returns
    -------
    neighs : list
        List of index pairs.
    """
    #Implement this function yourself
    #Delete the following line. Variables are set to None so that you can use
    #the module even if the function body is not defined.
    neighs=None
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

def recover(grid, i, j, beta):
    """ Determines if an individual at position (i, j) is going to recover during the current week.

    Parameters
    ----------
    grid : 2D numpy.ndarray
        Input grid on which to work.
    i : integer
        Row index of the individual.
    j : integer
        Column index of the individual.
    beta : float
        Model parameter giving the probability to recover during the week.

    Returns
    -------
    recovered : boolean
        Set to True if the individual at position (i, j) will be infected in current week. Otherwise False.
    """

    #Implement this function yourself
    #Delete the following line. Variables are set to None so that you can use
    #the module even if the function body is not defined.
    recovered=None
    return recovered

def plot2D_SIR(grid, title='SIR model'):
    """ Plots a 2D SIR model. When implementing, try to mimic the plots from the assignment instructions.

    Parameters
    ----------
    grid : 2D numpy.ndarray
        Grid storing the state of the 2D SIR model.
    title : str, optional
        Optional title of the plot
    """
    #Implement this function yourself
    return

def time_step(current_grid, alpha, beta):
    """ Performs a single step of 2D sir models with model parameters set by alpha and beta.

    Parameters
    ----------
    current_grid : 2D numpy.ndarray
        Grid representing the state of 2D SIR model in current week
    alpha : float
        Model parameter giving the probability to infection during the week.
    beta : float
        Model parameter giving the probability of recovery during the week.
    
    Returns
    -------
    new_grid : 2D numpy.ndarray
        Grid representing the 2D SIR model in next week, determined from the state given by teh current_grid argument.
    """
    #Implement this function yourself
    new_grid=current_grid.copy()

    return new_grid
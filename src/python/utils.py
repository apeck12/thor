
"""
Functions that are useful in various places, but have no common theme.
"""

from argparse import ArgumentParser
import pprint
import numpy as np


class odinparser(ArgumentParser):
    """
    Simple extension of argparse, designed to automatically print stuff
    """
    def parse_args(self):
        print graphic
        args = super(odinparser, self).parse_args()
        print args.__dict__
        return args


def smooth(x, beta=10.0, window_size=11):
    """
    Apply a Kaiser window smoothing convolution.
    
    Parameters
    ----------
    x : ndarray
        The array to smooth.
    beta : float
        Parameter controlling the strength of the smoothing -- bigger beta 
        results in a smoother function.
    window_size : int
        The size of the Kaiser window to apply, i.e. the number of neighboring
        points used in the smoothing.
    """
    
    # make sure the window size is odd
    if window_size % 2 == 0:
        window_size += 1
    
    # apply the smoothing function
    s = np.r_[x[window_size-1:0:-1], x, x[-1:-window_size:-1]]
    w = np.kaiser(window_size, beta)
    y = np.convolve( w/w.sum(), s, mode='valid' )
    
    # remove the extra array length convolve adds
    b = (window_size-1) / 2
    smoothed = y[b:len(y)-b]
    
    return smoothed

def arctan3(y, x):
    """ like arctan2, but returns a value in [0,2pi] """
    theta = np.arctan2(y,x)
    theta[theta < 0.0] += 2 * np.pi
    return theta


def write_sample_input(filename='sample.odin'):
    txt=''' # THIS FILE WAS GENERATED BY ODIN -- sample input file
    
    runname: testrun                 # used to name directories, etc.
    
    
    # RUN SETTINGS 
    predict:   boltzmann             # {single, boltzmann, kinetic} ensembles
    sampling:  md                    # either {md, mc} for dynamics, Monte Carlo
    prior:     minimal               # could be amber99sb-ildn, charm22, etc.
    solvent:   none                  # grand cannonical solvent to employ
    outputdir: ~/testrun             # where stuff gets written -- could be GB.
    
    
    # EXPERIMENTS
    experiment: LCLS_run_1           # a name identifying the data
        - dir:  ~/testrun/lcls       # should contain pre-processed data files
        - type: scattering           # {scattering, chemshift} are in now
    
    experiment: NMR_HSQC_1
        - dir:  ~/testrun/chemshifts
        - type: chemshift
        
        
    # RESOURCES
    runmode: cluster                 # one of {local, cluster}
    nodes:   4                       # how many nodes to call for
    gpn:     1                       # gpus per node
    REMD:    True                    # use REMD to estimate the lambdas
    temps:   [1, 0.5, 0.1, 0.01]     # temps in units of beta, <= nodes*gpn
    
    '''
    



graphic = """
	                                    .  
	                                  .#   
	           N                     .##   
	          #.                     #  :  
	       .# .                     .# .#  
	       .. |       ..##.         #   #  
	       #  l     .#.    #       #    #  
	             .#         #.    #    #   
	      #    #             #.  #.    #   
	      # .#                ##      #    
	      ##.                #7      :#       ____  _____ _____ _   _ 
	      #                 .# .:   .#       / __ \|  __ \_   _| \ | |
	   .:.  .   .    .      .#..   Z#       | |  | | |  | || | |  \| |
	  .####  . . ...####     #.   #.        | |  | | |  | || | | . ` |
	 # .##   . # . #.#   . ND .##.#         | |__| | |__| || |_| |\  |
	 . .#N   .  .   N.   # D .=#  #          \____/|_____/_____|_| \_|
	#   . ####     .###,  ,      ##        
	#.## .               7#7. # N  #                       Observation
	 .                      ##.. . #       	               Driven
	                          .#   #                       Inference
	                            #7 Z                   of eNsembles
		                        .#        

     ----------------------------------------------------------------------
"""

import FreeCAD

def QT_TRANSLATE_NOOP(context, text):
    return text

import TranslateUtils
from TranslateUtils import translate

import FreeCADGui
import os
LOCATION = os.path.join("Mod","FEMbyGEN","fembygen")
FreeCADGui.updateLocale()

"""
This code was originally published by the following individuals for use with
Scilab:
    Copyright (C) 2012 - 2013 - Michael Baudin
    Copyright (C) 2012 - Maria Christopoulou
    Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
    Copyright (C) 2009 - Yann Collette
    Copyright (C) 2009 - CEA - Jean-Marc Martinez
    
    website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

Much thanks goes to these individuals. It has been converted to Python by 
Abraham Lee.
"""

import numpy as np

__all__ = ['pbdesign']

def pbdesign(n):
    """
    Generate a Plackett-Burman design
    
    Parameter
    ---------
    n : int
        The number of factors to create a matrix for.
    
    Returns
    -------
    H : 2d-array
        An orthogonal design matrix with n columns, one for each factor, and
        the number of rows being the next multiple of 4 higher than n (e.g.,
        for 1-3 factors there are 4 rows, for 4-7 factors there are 8 rows,
        etc.)
    
    Example
    -------
    
    A 3-factor design::
    
        >>> pbdesign(3)
        array([[-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])
       
    A 5-factor design::
    
        >>> pbdesign(5)
        array([[-1., -1.,  1., -1.,  1.],
               [ 1., -1., -1., -1., -1.],
               [-1.,  1., -1., -1.,  1.],
               [ 1.,  1.,  1., -1., -1.],
               [-1., -1.,  1.,  1., -1.],
               [ 1., -1., -1.,  1.,  1.],
               [-1.,  1., -1.,  1., -1.],
               [ 1.,  1.,  1.,  1.,  1.]])
       
    """
    try:
        from scipy.linalg import toeplitz, hankel
        assert n>0, 'Number of factors must be a positive integer'
        keep = int(n)
        n = 4*(int(n/4) + 1)  # calculate the correct number of rows (multiple of 4)
        f, e = np.frexp([n, n/12., n/20.])
        k = [idx for idx, val in enumerate(np.logical_and(f==0.5, e>0)) if val]
        
        assert isinstance(n, int) and k!=[], 'Invalid inputs. n must be a multiple of 4.'
        
        k = k[0]
        e = e[k] - 1
        
        if k==0:  # N = 1*2**e
            H = np.ones((1, 1))
        elif k==1:  # N = 12*2**e
            H = np.vstack((np.ones((1, 12)), np.hstack((np.ones((11, 1)), 
                toeplitz([-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1],
                        [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1])))))
        elif k==2:  # N = 20*2**e
            H = np.vstack((np.ones((1, 20)), np.hstack((np.ones((19, 1)),
                hankel(
                [-1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1],
                [1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1])
                ))))
        
        # Kronecker product construction
        for i in range(e):
            H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))
        
        # Reduce the size of the matrix as needed
        H = H[:, 1:(keep + 1)]
        
        return np.flipud(H)
    except:
        print(translate("FEMbyGEN","You need to install scipy library to use it"))
        return None
    
    

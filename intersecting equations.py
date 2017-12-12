# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 11:18:56 2014

@author: donna
"""

"""
this could be useful for finding the two answers for the distance distribution
model.  We'd just need to re-write the distribution function so that x and y
are on the right.  And the other equation would be just a straight line where 
y = some number.
"""


# Consider the example of finding the intersection of a polynomial and a line:
# y1=x1^2
# y2=x2+1

from scipy.optimize import fsolve 
import math
import numpy as np

def f(x,y):
    x,y=xy   
    z = np.array([y-0.1711*math.exp(-((x-15.9)/6.042)**2), y-x-0.015366154])
    return z
 
fsolve(f,0,0)
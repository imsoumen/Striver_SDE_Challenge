from sys import *
from collections import *
from math import *

def printPascal(n):
    
    triangle = []
    
    for row in range(1, n+1):
        
        element = 1
        add = []
        
        for i in range(1, row+1):
            
            add.append(element)
            element = element * (row - i) // i
            
        triangle.append(add)
        
    return triangle

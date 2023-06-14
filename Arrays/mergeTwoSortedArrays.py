from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
   
    i, j = 0, 0

    while i < len(arr1) and j < n:
        if arr1[i] > arr2[j] or arr1[i] == 0:
            arr1.insert(i,arr2[j])
            j += 1
        else:
            i += 1

    arr1 = [i for i in arr1 if i != 0]

    return arr1

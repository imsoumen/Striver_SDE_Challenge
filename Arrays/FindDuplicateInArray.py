from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    freq = {}
    for i in range(0, n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            return arr[i]

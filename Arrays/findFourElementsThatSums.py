from math import *
from collections import *
from sys import *
from os import *

def commonIdx(p1, p2) :
    return p1[0] == p2[0] or p1[0] == p2[1] or p1[1] == p2[0] or p1[1] == p2[1]

def fourSum(arr, target):

    n = len(arr)
    map_sum = {}

    for i in range(n - 1):
        for j in range(i + 1, n):
            map_sum[arr[i] + arr[j]] = [i, j]
 
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if (target - sum) in map_sum and not commonIdx(map_sum[target - sum], [i, j]):
                return 'Yes'
    
    return 'No'

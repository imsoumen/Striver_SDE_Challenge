from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

    curSum = [0 for i in range(n)] 
    maxSum = 0
    for i in range(n) :
        if(i == 0) :
            curSum[i] = max(curSum[i], arr[i])
        else :
            curSum[i] = max(curSum[i], curSum[i-1] + arr[i])
        
        maxSum = max(maxSum, curSum[i])
    
    return maxSum

#taking input using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))

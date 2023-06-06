from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in range(n):
        if arr[i] == 0:
            cnt_0 += 1
        if arr[i] == 1:
            cnt_1 += 1
        if arr[i] == 2:
            cnt_2 += 1

    for i in range(cnt_0):
        arr[i] = 0
    
    for i in range(cnt_0, cnt_0+cnt_1):
        arr[i] = 1
    
    for i in range(cnt_0+cnt_1, n):
        arr[i] = 2


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)

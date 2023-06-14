from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	freq = {}
	N = len(arr)
	ans = []
	for i in range(N):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1
	
	
	for item in freq:
		if freq[item] > N//2:
			ans.append(item)

	if ans:
		return ans[0]
	else:
		return -1

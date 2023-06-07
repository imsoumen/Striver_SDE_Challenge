from os import *
from sys import *
from collections import *
from math import *

def merge(arr, low, mid, high):
    total = 0
    j = mid+1
    for i in range(low, mid+1):
        while j <= high and arr[i] > 2 * arr[j] :
            j += 1
        total += (j - (mid + 1))
    
    tmp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1
    
    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= high:
        tmp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i -low]
    
    return total

def mergeSort(arr, low, high):
    if low >= high:
        return 0

    mid = (low + high) // 2

    tmp = mergeSort(arr, low, mid)
    tmp += mergeSort(arr, mid+1, high)
    tmp += merge(arr, low, mid, high)

    return tmp


def reversePairs(arr, n):
    # Write your code here.
    return mergeSort(arr, 0, n-1)

    
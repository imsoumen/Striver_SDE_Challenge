from math import *
from collections import *
from sys import *
from os import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    # Write your code here.
    if not head:
        return head
    
    curr, n = head, 0

    while curr:
        n, curr = n+1, curr.next
    
    curr, i, prev = head, 0, Node(0)
    newHead  = prev

    while b:
        pos = b.pop(0)
        if pos == 0:
            continue
        
        if i+pos < n:
            pre, oldc = None, curr
            pos = i + pos

            while i < pos:
                temp = curr.next
                curr.next = pre
                pre, curr = curr, temp
                i += 1
            prev.next = pre
            oldc.next = curr
            prev = oldc
        
        elif i+pos >= n:
            pre, oldc = None, curr

            while curr:
                temp = curr.next
                curr.next = pre
                pre, curr = curr, temp
            
            prev.next  = pre
            prev = oldc
            oldc.next = None
            i=n
            break

    if i == 0:
        return head
    return newHead.next

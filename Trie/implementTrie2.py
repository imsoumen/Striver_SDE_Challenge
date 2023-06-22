from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.wordCount = 0
        self.prefixCount = 0
    
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self, char):
        return ord(char)-ord('a')

    def insert(self, word):
        curr = self.root
        for i in range (len(word)):
            index = self.getIndex(word[i])
            
            if curr.children[index] == None:
                curr.children[index] = TrieNode()                

            curr = curr.children[index]
            curr.prefixCount += 1
          
        curr.wordCount += 1   

    def countWordsEqualTo(self, word):
        curr = self.root

        for i in range (len(word)):
            index = self.getIndex(word[i])

            if curr.children[index] == None:
                return 0
               
            curr = curr.children[index]
            
        return curr.wordCount

    def countWordsStartingWith(self, word):
        curr = self.root

        for i in range (len(word)):
            index = self.getIndex(word[i])
           
            if curr.children[index] == None:
                return 0             

            curr = curr.children[index]

        return curr.prefixCount

    def erase(self, word):

        curr = self.root
        toBeDeleted = None

        for i in range (len(word)):
            index = self.getIndex(word[i])
            parent = curr
            curr = curr.children[index]

            curr.prefixCount -= 1

            if toBeDeleted:
                toBeDeleted = None
                
            if curr.prefixCount == 0:
                if not toBeDeleted:
                    parent.children[index] = None

                toBeDeleted = curr

            curr.wordCount -= 1

            if toBeDeleted:
                toBeDeleted = None

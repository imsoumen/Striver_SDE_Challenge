from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
        self.freq = 0

class Trie :

    def __init__(self) :
        # constructor for the Trie
        self.root = TrieNode()
    
    def getIndex(self, char):
        return ord(char)-ord('a')

    def insert(self, word) :
        # Insert function goes here
        curr = self.root
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        
        curr.eow = True

    def search(self, word) :
        # Search function goes here
        curr = self.root
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        
        return True if curr.eow == True else False

    def startWith(self, prefix) :
        # StartWith function goes here
        curr = self.root
        for i in range(len(prefix)):
            index = self.getIndex(prefix[i])
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        
        return True

# main
t = int(input().strip())
trie_obj = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        trie_obj.insert(str1)
    
    elif (q == 2) :
        if(trie_obj.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(trie_obj.startWith(str1)) :
            print("true")

        else :
            print("false")


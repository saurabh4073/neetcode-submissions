class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for char in s:
            hashS[char] = hashS.get(char,0) + 1
        
        for char in t:
            hashT[char] = hashT.get(char,0) +1
        
        return hashS==hashT
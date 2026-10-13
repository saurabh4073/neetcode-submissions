class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        if len(s)!=len(t):
            return False
            
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i],0) + 1
            hashT[t[i]] = hashT.get(t[i],0) +1         
        
        return hashS==hashT
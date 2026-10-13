class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string={}
        t_string={}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            s_string[s[i]] = s_string.get(s[i],0) +1
            t_string[t[i]] = t_string.get(t[i],0) +1
        
        return s_string==t_string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Count = [0]*26
        s2Count = [0]*26

        for char in s1:
            s1Count[ord(char)- ord('a')]+=1
        
        l=0
        for r in range(len(s2)):
            s2Count[ord(s2[r]) - ord('a')]+=1
            if (r-l+1)>len(s1):
                s2Count[ord(s2[l]) - ord('a')]-=1
                l+=1
            
            if s1Count==s2Count:
                return True
        return False
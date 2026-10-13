class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1count = [0]*26
        s2count = [0]*26

        for a in s1:
            s1count[ord(a)- ord('a')] +=1

        l=0
        for r in range(len(s2)):
            s2count[ord(s2[r]) - ord('a')] +=1

            if (r-l+1)>len(s1):
                s2count[ord(s2[l]) - ord('a')] -=1
                l+=1
            
            if s2count==s1count:
                return True
        return False
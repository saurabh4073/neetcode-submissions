class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = {}
        l,res =0,0

        for r in range(len(s)):
            if s[r] in charset:
                l= max(charset[s[r]]+1,l)
            charset[s[r]] = r
            res = max(res,r-l+1)
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        length = 0

        l=0
        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l+=1
            length = max(length, r-l+1)
            stringSet.add(s[r])
            print(stringSet, length, l , r)
        return length
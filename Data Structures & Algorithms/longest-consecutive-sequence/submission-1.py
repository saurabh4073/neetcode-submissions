class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest= 0

        for n in nums:
            if n-1 not in numset:
                length = 0
                while (length+n) in numset:
                    length+=1
                longest= max(longest,length)
        return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in numsset:
                length = 0
                while n+length in numsset:
                    length+=1
                longest=max(longest,length)
        return longest

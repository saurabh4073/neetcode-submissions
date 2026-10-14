class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for n in numset:
            if n-1 in numset:
                continue
            length=0
            k = n
            while k in numset:
                length+=1
                k+=1
            res = max(length,res)
        
        return res


        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}

        for i,n in enumerate(nums):
            if target-n in hashm:
                return [hashm[target-n], i]
            hashm[n]=i
        
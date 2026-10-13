class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numarr = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numarr:
                return [numarr[diff], i]
            else:
                numarr[nums[i]] = i
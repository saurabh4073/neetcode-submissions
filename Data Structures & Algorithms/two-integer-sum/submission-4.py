class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numArr = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numArr:
                return [numArr[diff],i]
            else:
                numArr[nums[i]] = i
         
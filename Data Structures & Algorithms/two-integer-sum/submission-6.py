class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hashmap:
                return [hashmap[num2],i]
            hashmap[nums[i]] = i
        
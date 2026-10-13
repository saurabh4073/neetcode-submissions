class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            b = target-nums[i]
            if b in cache:
                return [cache[b], i]
            cache[nums[i]] = i
        
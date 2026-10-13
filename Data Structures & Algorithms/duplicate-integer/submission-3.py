class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr1 = {}
        for n in nums:
            if n in arr1:
                return True
            else:
                arr1[n]=n
        return False
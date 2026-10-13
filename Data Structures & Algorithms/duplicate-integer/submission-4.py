class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numArr = {}
        for i in nums:
            if i not in numArr:
                numArr[i]=i
            else:
                return True
        return False

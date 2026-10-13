class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        dp = set()
        dp.add(0)
        target= sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            tmpdp = dp.copy()
            for t in dp:
                if t == target or (t+nums[i])==target:
                    return True
                if (t+nums[i]) not in tmpdp:
                    tmpdp.add(t+nums[i])
                if t not in tmpdp:
                    tmpdp.add(t)
            dp=tmpdp
        return False
                
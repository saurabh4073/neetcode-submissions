class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def maxrob(tempnums):
            rob1,rob2=0,0

            for n in tempnums:
                temp = max(rob1+ n,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        

        return max(nums[0],maxrob(nums[1:]),maxrob(nums[:-1]))
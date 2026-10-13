class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        l,r = 0, len(height)-1
        leftmax, rightMax = height[l],height[r]
        res = 0 
        while l<r:
            if leftmax<rightMax:
                l+=1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r-=1
                rightMax = max(rightMax , height[r])
                res+= rightMax - height[r]
        return res
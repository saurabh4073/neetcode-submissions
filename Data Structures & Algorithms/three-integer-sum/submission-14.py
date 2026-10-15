class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            # l,r= i+1,len(nums)-1
            # while l<r:
            #     total = a + nums[l] + nums[r]

            #     if total<0:
            #         l+=1
            #     elif total>0:
            #         r-=1
            #     else:
            #         res.append([a,nums[l],nums[r]])
            #         l+=1

            #         while l<r and nums[l]==nums[l-1]:
            #             l+=1

            # a+b+c = 0
            # a = -b-c
            hashmap= {}
            for j in range(i+1,len(nums)):
                num3 = 0 - a - nums[j]
                if num3 in hashmap and ((len(res) and res[-1]!=[a,nums[j],num3]) or not len(res)):
                    res.append([a,nums[j],num3])
                hashmap[nums[j]]=nums[j]
        return res

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-n for n in nums]
        heapq.heapify(minheap)
        res =0
        while k>0:
            res = -(heapq.heappop(minheap))
            k-=1
        return res
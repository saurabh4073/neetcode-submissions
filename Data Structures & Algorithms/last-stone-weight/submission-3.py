class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapstone = [-s for s in stones]
        heapq.heapify(heapstone)
        while len(heapstone)>1:
            first = abs(heapq.heappop(heapstone))
            second = abs(heapq.heappop(heapstone))
            if first>second:
                heapq.heappush(heapstone, -(first-second))
        
        return abs(heapstone[0]) if heapstone else 0
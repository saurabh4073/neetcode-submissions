class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hstones = [-s for s in stones]
        heapq.heapify(hstones)
        
        while len(hstones)>1:
            first = abs(heapq.heappop(hstones))
            second = abs(heapq.heappop(hstones))
            if first>second:
                heapq.heappush(hstones, -(first-second))
        return abs(hstones[0]) if hstones else 0

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        premap = defaultdict(list)

        for u,v,w in times:
            premap[u].append((v,w))
        
        minheap = [(0,k)]
        heapq.heapify(minheap)
        visit = set()
        t=0
        while minheap:
            w,n2 = heapq.heappop(minheap)
            if n2 in visit:
                continue
            visit.add(n2)
            t=max(t,w)

            for n1,w1 in premap[n2]:
                if n1 not in visit:
                    heapq.heappush(minheap,(w1+w,n1))
        return t if len(visit)==n else -1

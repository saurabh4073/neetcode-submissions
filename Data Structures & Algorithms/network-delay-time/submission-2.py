class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))
        
        visit=set()
        minheap=[(0,k)]
        heapq.heapify(minheap)
        t=0
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                    continue
            t= max(t,w1)

            visit.add(n1)
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(w2+w1,n2))
        return t if len(visit)==n else -1
            

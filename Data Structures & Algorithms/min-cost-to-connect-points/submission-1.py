class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        
        res=0
        visit = set()
        minheap = [(0,0)]
        heapq.heapify(minheap)

        while len(visit)!=len(points):
            dist, p1 = heapq.heappop(minheap)

            if p1 in visit:
                continue
            res+=dist
            visit.add(p1)
            for nc, n  in adj[p1]:
                if n not in visit:
                    heapq.heappush(minheap,(nc,n))
        return res

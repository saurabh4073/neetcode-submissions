class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        visit= set()

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist= abs(x2-x1) + abs(y2-y1)
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        
        minheap = [(0,0)]
        heapq.heapify(minheap)
        while len(visit)!=len(points):
            d,x = heapq.heappop(minheap)
            if x in visit:
                continue
            res += d
            visit.add(x)
            for d2,x2 in adj[x]:
                if x2 not in visit:
                    heapq.heappush(minheap, (d2,x2))
        return res
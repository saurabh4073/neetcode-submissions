class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counttask = {}
        for t in tasks:
            counttask[t] = 1 + counttask.get(t,0)
        maxheap = [-t for t in counttask.values()]
        heapq.heapify(maxheap)
        q= deque([])
        t=0
        
        while q or maxheap:
            t+=1
            task = -(heapq.heappop(maxheap)) if maxheap else 0
            task -=1
            if task>0:
                q.append([-task, t+n])
            
            if q and q[0][1]==t:
                task,time = q.popleft()
                heapq.heappush(maxheap, task)
            
        return t
        

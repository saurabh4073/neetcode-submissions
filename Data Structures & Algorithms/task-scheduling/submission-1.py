class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for t in tasks:
            if t not in count:
                count[t]=0
            count[t]+=1
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        t=0
        q=deque([])
        while maxheap or q:
            t+=1
            task = -(heapq.heappop(maxheap)) if maxheap else 0
            if task:
                task-=1
                if task>0:
                    q.append([task,t+n])
            if q and q[0][1]==t:
                heapq.heappush(maxheap,-(q.popleft()[0]))
        return t

        

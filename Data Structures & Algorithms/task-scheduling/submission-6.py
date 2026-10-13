class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t]=1+count.get(t,0)
        minheap=[-s for s in count.values()]
        heapq.heapify(minheap)
        t=0
        q=deque([])
        while q or minheap:
            t+=1
            task=-(heapq.heappop(minheap)) if minheap else 0
            task-=1
            if task>0:
                q.append([-task,t+n])
            if q and q[0][1]==t:
                task,time=q.popleft()
                heapq.heappush(minheap,task)
        return t


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counttasks={}
        for t in tasks:
            if t not in counttasks:
                counttasks[t]=0
            counttasks[t]+=1
        maxheap= [-c for c in counttasks.values()]
        heapq.heapify(maxheap)

        t=0
        q=deque([])
        while maxheap or q:
            t+=1
            task = -(heapq.heappop(maxheap)) if maxheap else 0
            task-=1
            if task>0:
                q.append([-task,t+n])
            if q and q[0][1]==t:
                heapq.heappush(maxheap,q.popleft()[0])
        return t

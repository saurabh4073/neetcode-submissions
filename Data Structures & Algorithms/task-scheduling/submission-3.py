class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counttask = {}
        for t in tasks:
            if t not in counttask:
                counttask[t] = 0
            counttask[t] +=1 
        minheap = [-t for t in counttask.values()]
        heapq.heapify(minheap)
        q = deque([])
        t=0
        while q or minheap:
            t+=1
            task = -(heapq.heappop(minheap)) if minheap else 0
            task-=1
            if task>0:
                q.append([task, t+n])
            if q and q[0][1]==t:
                task,time = q.popleft()
                print(task)
                heapq.heappush(minheap,-task)
            
        return t


        

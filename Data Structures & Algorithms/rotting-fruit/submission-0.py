class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        q=deque([])
        rows, cols = len(grid), len(grid[0])
        fresh_oranges=0
        rotten_oranges=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_oranges+=1
                elif grid[r][c]==2:
                    rotten_oranges+=1
                    q.append((r,c))
                    visit.add((r,c))
        time=0
        directions= [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh_oranges>0:
            for i in range(len(q)):
                row,col = q.popleft()

                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]==1:
                        q.append((r,c))
                        fresh_oranges-=1
                        visit.add((r,c))
            time+=1
        return time if fresh_oranges==0 else -1
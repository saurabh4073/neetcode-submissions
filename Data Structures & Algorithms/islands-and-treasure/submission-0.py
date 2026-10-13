class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid),len(grid[0])

        dist=0
        q=deque([])
        visit=set()

        def bfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==-1 or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            
            dist+=1
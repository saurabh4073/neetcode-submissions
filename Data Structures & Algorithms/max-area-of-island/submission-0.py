class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxAIsland= 0
        rows,cols = len(grid), len(grid[0])  
        visit=set()

        def bfs(r,c):
            visit.add((r,c))
            q=deque([(r,c)])
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            islandSize=1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]==1:
                        visit.add((r,c))
                        islandSize+=1
                        q.append((r,c))
            return islandSize

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxAIsland= max(maxAIsland,bfs(r,c))

        return maxAIsland

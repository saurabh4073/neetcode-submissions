class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxisland = 0
        visit= set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q=deque([(r,c)])
            islandSize=1
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = dr+row, dc+col
                    if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visit:
                        islandSize+=1
                        visit.add((r,c))
                        q.append((r,c))
            return islandSize

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxisland=max(maxisland,bfs(r,c))
        return maxisland
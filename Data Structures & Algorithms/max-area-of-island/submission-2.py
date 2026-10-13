class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit =set()
        q= deque([])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islandArea = 0

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            islanda= 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = dr+row,dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]==1:
                        islanda+=1
                        q.append((r,c))
                        visit.add((r,c))
            return  islanda

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    islandArea= max(islandArea,bfs(r,c))
        return islandArea
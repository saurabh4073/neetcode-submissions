class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit= set()
        q=deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        dist=0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col]=dist
                for dr,dc in directions:
                    r,c=dr+row, dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]!=-1:
                        q.append((r,c))
                        visit.add((r,c))
            dist+=1


        
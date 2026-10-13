class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque([])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        freshf= 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c]==1:
                    freshf+=1
        t=0
        while q and freshf:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]==1:
                        q.append((r,c))
                        visit.add((r,c))
                        freshf-=1
            t+=1
        return t if freshf==0 else -1

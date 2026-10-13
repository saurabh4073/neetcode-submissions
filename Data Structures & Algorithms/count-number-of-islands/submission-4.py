class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        visit= set()

        def bfs(r,c):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            q=deque([(r,c)])
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]=="1":
                        visit.add((r,c))
                        q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)
        return islands

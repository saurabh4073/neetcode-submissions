class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visit=set()
        island=0
        
        def bfs(r,c):
            q=deque([(r,c)])
            visit.add((r,c))

            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c=dr+row,dc+col

                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island

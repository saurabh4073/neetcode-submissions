class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid),len(grid[0])
        visit= set()
        q = deque([])
        island= 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c= dr+row,dc+col

                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]=="1":
                        q.append((r,c))
                        visit.add((r,c))
            return


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    island+=1
                    bfs(r,c)
        return island
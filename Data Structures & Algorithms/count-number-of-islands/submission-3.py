class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit=set()
        islands=0

        def bfs(r,c):
            stack=[(r,c)]
            visit.add((r,c))
            directions=[[0,1],[0,-1],[1,0],[-1,0]]

            while stack:
                row,col = stack.pop()
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit:
                        stack.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)
        
        return islands

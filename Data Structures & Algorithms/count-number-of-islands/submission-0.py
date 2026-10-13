class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        path = set()

        def bfs(r, c):
            q = []
            q.append((r, c))
            path.add((r, c))
            while q:
                row, col = q.pop(0)
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr , nc = row + dr, col + dc
                    if (nr in range(rows) and
                        nc in range(cols) and 
                        grid[nr][nc] == '1' and
                        (nr, nc) not in path):
                        q.append((nr, nc))
                        path.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in path:
                    bfs(r,c)
                    islands +=1
        return islands
                
        
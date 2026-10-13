class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def bfs(r,c,visit):
            q=deque([])
            q.append((r,c))
            visit.add((r,c))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    for dr,dc in directions:
                        r,c = dr+row,dc+col
                        if r in range(rows) and c in range(cols) and heights[r][c]>=heights[row][col] and (r,c) not in visit:
                            q.append((r,c))
                            visit.add((r,c))
            return

        for c in range(cols):
            bfs(0,c,pac)
            bfs(rows-1,c,atl)

        for r in range(rows):
            bfs(r,0,pac)
            bfs(r,cols-1,atl)
        
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
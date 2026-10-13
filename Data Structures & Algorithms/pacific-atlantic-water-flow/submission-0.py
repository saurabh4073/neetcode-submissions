class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def bfs(r1,c1,visit):
            q = deque([])
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            q.append((r1,c1))
            visit.add((r1,c1))
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    for dr,dc in directions:
                        r,c=row+dr,dc+col
                        if r in range(rows) and c in range(cols) and heights[r][c]>=heights[row][col] and (r,c) not in visit:
                            q.append((r,c))
                            visit.add((r,c))
            


        #first row and last row
        for c in range(cols):
            bfs(0,c,pac)
            bfs(rows-1,c,atl)

        #first col and last col
        for r in range(rows):
            bfs(r,0,pac)
            bfs(r,cols-1,atl)
        
        res= []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

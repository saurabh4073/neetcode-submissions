class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl= set()
        pac = set()
        atlq = deque([])
        pacq = deque([])

        for r in range(rows):
            pacq.append((r,0))
            atlq.append((r,cols-1))
        
        for c in range(cols):
            pacq.append((0,c))
            atlq.append((rows-1,c))
        
        def bfs(q,visit):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    visit.add((row,col))
                    for dr,dc in directions:
                        r,c = dr+row,dc+col
                        if r in range(rows) and c in range(cols) and (r,c) not in visit and heights[r][c]>=heights[row][col]:
                            q.append((r,c))
            return 
        
        bfs(pacq,pac)
        bfs(atlq,atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

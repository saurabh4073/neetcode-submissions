class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pacset = set()
        atlset =set()
        pacq= deque([])
        atlq = deque([])
        res =[]
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            atlq.append((r,cols-1))
            pacq.append((r,0))
        
        for c in range(cols):
            pacq.append((0,c))
            atlq.append((rows-1,c))
        
        def bfs(visit, q):
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    visit.add((row,col))
                    for dr,dc in directions:
                        r,c = row+dr,dc+col
                        if r in range(rows) and c in range(cols) and (r,c) not in visit and heights[r][c]>=heights[row][col]:
                            q.append((r,c))
            return
        
        bfs(pacset,pacq)
        bfs(atlset,atlq)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacset and (r,c) in atlset:
                    res.append([r,c])
        return res

        
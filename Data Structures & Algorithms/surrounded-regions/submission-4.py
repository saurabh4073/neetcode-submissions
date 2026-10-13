class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols= len(board),len(board[0])
        q=deque([])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            if board[r][0]=="O":
                q.append((r,0))
            if board[r][cols-1]=="O":
                q.append((r,cols-1))
        
        for c in range(cols):
            if board[0][c]=="O":
                q.append((0,c))
            if board[rows-1][c]=="O":
                q.append((rows-1,c))
        
        while q:
            row,col=q.popleft()
            if board[row][col]=="O":
                board[row][col]="T"
            for dr,dc in directions:
                r,c=dr+row,dc+col
                if r in range(rows) and c in range(cols) and board[r][c]=="O":
                    q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"
            
        




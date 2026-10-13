class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q= deque([])
        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c]=='O':
                    q.append((r,c))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            row,col = q.popleft()
            if board[row][col]=='O':
                board[row][col]='T'
            for dr,dc in directions:
                r,c = dr+row,dc+col
                if r in range(rows) and c in range(cols) and board[r][c]=='O':
                    q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'
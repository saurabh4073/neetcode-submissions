class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = collections.defaultdict(set)
        # cols = collections.defaultdict(set)
        # squares = collections.defaultdict(set)
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                if r not in rows:
                    rows[r]=set()
                if c not in cols:
                    cols[c]=set()
                if (r//3,c//3) not in squares:
                    squares[(r//3),(c//3)]=set()
                    
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3,c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True

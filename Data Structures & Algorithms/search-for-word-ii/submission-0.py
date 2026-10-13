class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def createTree(self,word):
        curr= self

        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.endOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        rows, cols = len(board),len(board[0])
        for w in words:
            root.createTree(w)
        
        res,visit= set(),set()

        def dfs(r,c,node,word):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
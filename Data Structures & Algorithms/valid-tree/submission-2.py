class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        premap = {}
        for i in range(n):
            premap[i]=[]
        
        for n1,n2 in edges:
            premap[n1].append(n2)
            premap[n2].append(n1)
        
        visit=set()

        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for node in premap[curr]:
                if node == prev:
                    continue
                
                if not dfs(node,curr):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n
                
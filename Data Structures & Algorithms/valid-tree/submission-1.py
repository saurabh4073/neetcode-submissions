class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        premap={}
        for i in range(n):
            premap[i]=[]
        for e1,e2 in edges:
            premap[e1].append(e2)
            premap[e2].append(e1)

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

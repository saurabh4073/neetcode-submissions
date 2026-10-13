class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        premap = {}
        visit= set()
        for i in range(n):
            premap[i]=[]
        
        for n1,n2 in edges:
            premap[n1].append(n2)
            premap[n2].append(n1)
        
        def dfs(curr,prev):
            if curr in visit:
                return False
            
            visit.add(curr)
            for pre in premap[curr]:
                if pre==prev:
                    continue
                
                if not dfs(pre,curr):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n 

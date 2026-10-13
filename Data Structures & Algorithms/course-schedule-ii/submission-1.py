class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap= {}
        for i in range(numCourses):
            premap[i]=[]
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        visit=set()
        res = []
        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs]==[]:
                res.append(crs) if crs not in res else None
                return True
            
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            res.append(crs)
            premap[crs]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

        

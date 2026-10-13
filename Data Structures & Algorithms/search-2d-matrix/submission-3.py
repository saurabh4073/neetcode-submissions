class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL= len(matrix),len(matrix[0])
        top, bot= 0, ROW-1
        while top<=bot:
            m=(top+bot)//2
            if target>matrix[m][-1]:
                top=m+1
            elif target<matrix[m][0]:
                bot=m-1
            else: 
                break
        if top>bot:
            return False
        
        l,r= 0, COL-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[m][mid]:
                l=mid+1
            elif target<matrix[m][mid]:
                r=mid-1
            elif target==matrix[m][mid]:
                return True
        return False
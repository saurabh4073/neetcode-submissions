class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        top, bot= 0, ROWS-1
        while top<=bot:
            mid = (top+bot)//2
            if target> matrix[mid][-1]:
                top=mid+1
            elif target< matrix[mid][0]:
                bot=mid-1
            else:
                break
        if top>bot:
            return False
        
        l,r=0, COLS-1
        while l<=r:
            m = (l+r)//2
            if matrix[mid][m]<target:
                l=m+1
            elif matrix[mid][m]>target:
                r=m-1
            elif matrix[mid][m]==target:
                return True
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            lnum, rnum = matrix[i][0], matrix[i][len(matrix[i])-1]
            print("here",lnum,rnum)
            if lnum <= target and rnum>= target:
                l,r = 0, len(matrix[i])-1
                while l<=r:
                    m= (l+r)//2
                    print("mat",matrix[i][m],target )
                    if matrix[i][m]<target:
                        l=m+1
                    elif matrix[i][m]>target:
                        r=m-1
                    elif matrix[i][m] == target:
                        return True
        return False
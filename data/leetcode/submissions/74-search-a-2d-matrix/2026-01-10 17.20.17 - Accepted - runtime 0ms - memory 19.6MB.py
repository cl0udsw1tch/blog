class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N=len(matrix),len(matrix[0])

        P=lambda x : (matrix[x//N][x%N]<target)

        l,r=-1,M*N
        while r>l+1:
            MID=(l+r)//2
            if P(MID):
                l=MID
            else:
                r=MID

        return r<M*N and matrix[r//N][r%N]==target

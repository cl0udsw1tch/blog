class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        M,N=len(matrix),len(matrix[0])
        if M==1 and N==1:
            return
        
        for m in range(M):
            zero_in_row=False
            for n in range(N):
                num=matrix[m][n]
                if num in [0,'b']:
                    zero_in_row=True
                    for mp in range(M):
                        matrix[mp][n] = 'a' if matrix[mp][n] not in [0, 'b'] else 'b'
            if zero_in_row:
                matrix[m]=['a' if num not in [0,'b'] else 'b' for num in matrix[m]]
        for m in range(M):
            for n in range(N):
                if matrix[m][n] in ['a', 'b']:
                    matrix[m][n]=0
     

        
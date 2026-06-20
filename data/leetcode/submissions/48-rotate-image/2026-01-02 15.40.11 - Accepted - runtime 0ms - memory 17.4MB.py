class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M=len(matrix)
        if M==1: return
        for depth in range(M//2):
            MIN,MAX=depth,M-depth-1
            n_nums=(M-depth*2)*4-4
            n_groups=n_nums//4

            for k in range(n_groups):
                prev_i,prev_j=MAX-k,MIN
                curr_i,curr_j=MIN,MIN+k
                prev,curr=matrix[prev_i][prev_j], matrix[curr_i][curr_j]
                for l in range(4):
                    matrix[curr_i][curr_j]=prev
                    
                    #corners
                    if k==0:
                        if (curr_i,curr_j)==(MIN,MIN):
                            curr_i,curr_j=MIN,MAX
                        elif (curr_i,curr_j)==(MIN,MAX):
                            curr_i,curr_j=MAX,MAX
                        elif (curr_i,curr_j)==(MAX,MAX):
                            curr_i,curr_j=MAX,MIN
                        elif (curr_i,curr_j)==(MAX,MIN):
                            curr_i,curr_j==MIN,MIN
                    #edges
                    else:
                        if curr_i==MIN:
                            curr_i,curr_j=curr_j,MAX
                        elif curr_j==MAX:
                            curr_i,curr_j=MAX,MAX-(curr_i-MIN)
                        elif curr_i==MAX:
                            curr_i,curr_j=curr_j,MIN
                        elif curr_j==MIN:
                            curr_i,curr_j=MIN,MAX-(curr_i-MIN)

                    prev=curr
                    curr=matrix[curr_i][curr_j]
        return

                


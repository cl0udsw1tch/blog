class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==1: return 1

        def backtrack(row,row_mask,col_mask,diagA_mask, diagB_mask):
            if row==n: return 1

            count=0
            for col in range(n):
                x,y=row,col
                if (1<<x)&row_mask: continue
                if (1<<y)&col_mask: continue
                if (1<<(x+y))&diagA_mask: continue
                if (1<<(n-x-1 + y))&diagB_mask: continue
                row_mask_p,col_mask_p=(1<<x)|row_mask,(1<<y)|col_mask
                diagA_mask_p,diagB_mask_p=(1<<(x+y))|diagA_mask,(1<<(n-x-1+y))|diagB_mask
                count+=backtrack(row+1,row_mask_p,col_mask_p,diagA_mask_p,diagB_mask_p)
            return count 

        return backtrack(0,0,0,0,0) 

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0: return 0
        if poured==1: return int(query_row==0)

        memo={}
        VOL,EXCESS=0,1
        memo[(0,0)]=(1,poured-1)
        def dfs(s):
            if s in memo: return
            i,j=s

            if 0<j<i:
                dfs((i-1,j-1))
                dfs((i-1,j))
                total=0.5*memo[(i-1,j-1)][EXCESS] + 0.5*memo[(i-1,j)][EXCESS]
            elif j==0:
                dfs((i-1,j))
                total=0.5*memo[(i-1,j)][EXCESS]
            else:
                dfs((i-1,j-1))
                total=0.5*memo[(i-1,j-1)][EXCESS]

            vol=min(1,total)
            excess=total-vol
            memo[s]=vol,excess


        dfs((query_row, query_glass))
        return memo[(query_row, query_glass)][VOL]

            
            
            


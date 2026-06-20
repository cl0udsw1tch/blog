class Solution:
    def numTrees(self, n: int) -> int:
        '''
        stage_m: m=1...n subproblem f*_m(s_m) solves the problem for [m...s_m]
        x_m: which in [m...s_m] is the root
        f_m(s_m, x_m) = f*_m(x_m-1) * f*_{x_m+1}(s_m)
        '''

        if n<=2:
            return n
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[-1][-1]=1
        dp[-2][-1]=2
        dp[-2][-2]=1

        for m in range(n-3,-1,-1):

            for s_m in range(m, n):
                
                if s_m==m:
                    dp[m][s_m]=1
                    continue
                elif s_m==m+1:
                    dp[m][s_m]=2
                    continue
                else:
                    F=[]
                    F.append(1*dp[m+1][s_m])
                    for x_m in range(m+1, s_m):
                        F.append(dp[m][x_m-1]*dp[x_m+1][s_m])
                    F.append(dp[m][s_m-1]*1)

                    dp[m][s_m]=sum(F)
                    
        return dp[0][-1]


        
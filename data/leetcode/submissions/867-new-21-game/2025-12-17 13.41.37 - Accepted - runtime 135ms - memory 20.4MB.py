class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        M=k+maxPts
        dp= [[(0,0)] for _ in range(M)]
        dp[-1][0]=(int(M-1<=n), 0) #prob, rolling sum m+1...m+maxPts

        for m in range(M-2, -1, -1):
            stage_m=dp[m]
            s_m=0

            if m>=k:
                stage_m[s_m]=(int(m<=n), dp[m+1][s_m][0]+dp[m+1][s_m][1])
            elif m==k-1:
                newSum=dp[m+1][s_m][0]+dp[m+1][s_m][1]
                stage_m[s_m]=((1/maxPts)*newSum, newSum)
            else:
                newSum=dp[m+1][s_m][0]+dp[m+1][s_m][1]-dp[m+1+maxPts][s_m][0]
                stage_m[s_m]=((1/maxPts)*newSum, newSum)
        return dp[0][0][0]
                

        memo={}

        def dfs(s):
            if s in memo: return

            if s >= k:
                memo[s] = int(s<=n)
                return
            F=[0]*maxPts
            for x in range(1, maxPts+1):
                s_p=s+x
                dfs(s_p)
                f=(1/maxPts)*memo[s_p]
                F[x-1]=f
            memo[s]=sum(F)
            
        dfs(0)
        return memo[0]

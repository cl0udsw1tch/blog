class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        stage_m: m=0..M-1 subproblem f*_m(s_m) solves the problem for leaves [m...s_m]
        x_m: the leaf in (m...s_m) that starts the right subtree for the nearest common ancestor of m,s_m
        f_m(s_m, x_m) = f*_m(x_m-1) + max(arr[m]...arr[x_m-1]) * max(arr[x_m]...arr[s_m]) * f_{x_m}(s_m)
        '''

        M=len(arr)
        if M==2:
            return math.prod(arr)

        N=M
        dp = [[0 for _ in range(N)] for _ in range(M)]
        dp[-2][-1] = math.prod(arr[-2:])
        for m in range(M-3,-1,-1):
            for s_m in range(m+1, N):
                if s_m==m+1:
                    dp[m][s_m]=math.prod(arr[m:s_m+1])
                    continue
                else:
                    F = []
                    for x_m in range(m+1,s_m+1):
                        F.append(dp[m][x_m-1] + max(arr[m:x_m])*max(arr[x_m:s_m+1]) + dp[x_m][s_m])
                    dp[m][s_m]=min(F)

        return dp[0][-1]


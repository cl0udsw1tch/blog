class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        stage_m: m=0...M subproblem f*_m(s_m, t_m) solves the problem after 0..m-1 digits have been filled and have mask
                    s_m and the current position m's tightness is given by t_m
        s_m: 0...1<<10-1 mask of digits 0-9 used from 0...m-1
        t_m: non-tight (0) or tight (1)
        => (if x_m==0 and s_m == 0) s_{m+1} = 0 (digit has yet to start, mask still empty)
        => (else) s_{m+1} = 1 << x_m | s_m (valid if not 1<<x_m & s_m)
        => t_{m+1} = t_m AND x_m==num[m]
        f_m(s_m, t_m, x_m) = f*_{m+1}(s_{m+1}, t_{m+1})
        f*_m(s_m, t_m) = sum_{x_m if not 1<<x_m & s_m} (f_m(s_m, t_m, x_m))
        '''
        if n==0: return 1
        if n==1: return 10

        num=10**n - 1
        str_n = str(num)
        arr=[int(c) for c in str_n]
        M=len(arr)

        dp = [[[0, 0] for _ in range(1<<10)] for _ in range(M+1)]
    
        for s_m in range(1<<10):
            dp[M][s_m][0] = 1
            dp[M][s_m][1] = 1

        for m in range(M-1, -1, -1):
            for s_m in range(1<<10):
                for t_m in range(2):
                    limit = arr[m] if t_m else 9
                    F=[0]*(limit+1)
                    for x_m in range(0, limit+1):
                        if s_m & (1 << x_m):
                            continue
                        s_mp1 = 0 if (x_m == 0 and s_m == 0) else s_m | (1 << x_m)
                        t_mp1 = t_m and (x_m == limit)
                        F[x_m] = (dp[m+1][s_mp1][t_mp1])

                    f_sum=sum(F)
                    dp[m][s_m][t_m] = f_sum

        return dp[0][0][1]


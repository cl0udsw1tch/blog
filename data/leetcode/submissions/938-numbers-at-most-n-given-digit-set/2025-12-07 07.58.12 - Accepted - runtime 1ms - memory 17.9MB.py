class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        '''
        stage_m: m=0...M-1 subproblem solution f*_m(s_m) solves the problem of how many numbers
        are less than n with the first m digits being t_m tight
        s_m: [not]tight
        x_m: digit 
        s_mp1=s_m AND (x_m==n[m])
        f_m(s_m, x_m) = f*_{m+1}(s_mp1)
        f*_m(s_m) = sum_{x_m}(f_m(s_m, x_m))
        '''

        str_n=str(n)
        arr_n=list(map(int, str_n))
        digits=list(map(int, digits))
        D=len(digits)
        M=len(arr_n)
        if n==1:
            return int(1 in digits)

        dp=[[0,0] for _ in range(M)]

        m=M-1
        stage_m=dp[m]
        for s_m in range(2):
            limit=arr_n[-1] if s_m else 9
            F=[]
            for x_m in digits:
                if x_m > limit: break
                F.append(1)
            f_sum=sum(F)
            stage_m[s_m]=f_sum

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]

            for s_m in range(2):
               
                limit=arr_n[m] if s_m else 9
                F=[]

                for x_m in digits:
                    if x_m > limit: break
                    s_mp1=int(s_m and arr_n[m]==x_m)
                    F.append(stage_mp1[s_mp1])
                f_sum=sum(F)

                stage_m[s_m]=f_sum

        return dp[0][1] + sum([dp[i][0] for i in range(1, M)])
        
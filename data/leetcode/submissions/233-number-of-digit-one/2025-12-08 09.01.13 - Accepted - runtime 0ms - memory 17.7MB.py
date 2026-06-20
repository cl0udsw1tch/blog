class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        stage_m: m=0..M-1 subproblem f*_m(s_m)[:2] solves the total # of 1s and # of numbers in n[m...M-1] for a given
        tightness s_m
        s_m: not tight(0) or tight(1) bounds on the current digit
        x_m: picking a digit at the current position
        f_m(s_m, x_m)[0] = f*_{m+1}(s_{m+1})[0] + (f*_{m+1}(s_{m+1})[1] if x_m==1 else 0)
        f_m(s_m, x_m)[1] = f*_{m+1}(s_{m+1})[1]
        f*_m(s_m) = sum_{x_m}(f_m(s_m, x_m))
        '''

        
        if n==0:
            return 0
        if n<10:
            return 1
        arr_n=list(map(int, str(n)))
        M=len(arr_n)

        dp=[[(0,0) for _ in range(2)] for _ in range(M)]
        m=M-1
        stage_m=dp[m]
        for s_m in range(2):
            F=[]
            limit=arr_n[m] if s_m else 9
            for x_m in range(limit+1):
                f=(0,1) if x_m != 1 else (1,1)
                F.append(f)
            f_sum=(sum([f[0] for f in F]), sum([f[1] for f in F]))
            stage_m[s_m]=f_sum
            
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            for s_m in range(2):
                F=[]
                limit=arr_n[m] if s_m else 9
                for x_m in range(limit+1):
                    s_mp1=s_m and (x_m == limit)
                    f_mp1=stage_mp1[s_mp1]
                    f=(f_mp1[0], f_mp1[1]) if x_m != 1 else (f_mp1[0] + f_mp1[1], f_mp1[1])
                    F.append(f)
                f_sum=(sum([f[0] for f in F]), sum([f[1] for f in F]))
                stage_m[s_m]=f_sum

        return dp[0][1][0]

     


        


        
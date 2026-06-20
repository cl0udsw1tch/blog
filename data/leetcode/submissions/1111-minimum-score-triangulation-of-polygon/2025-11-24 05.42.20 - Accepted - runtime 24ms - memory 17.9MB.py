class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for values[m...s_m]
        s_m: terminal vertex
        x_m: the interior vertex (in (m,s_m)) of the triangle containing m,s_m. 
        (x_m=m+1) f_m(s_m, x_m) = f*_{m+1}(s_m) values[s_m-1]*values[s_m]*values[m]
        (x_m=s_m-1) f_m(s_m, x_m) =  f*_m(s_m-1) + values[s_m]*values[m]*values[m+1]
        (x_m in (m+1,s_m-1)) f_m(s_m, x_m) = values[m]*values[s_m]*values[x_m] + f*_m(x_m) + f*_{x_m}(s_m)
        f*_m(s_m) = \min_{s_m}(f_m(s_m,x_m))

        '''

        M=len(values)
        if M==3:
            return math.prod(values)

        if M==4:
            return min(math.prod(values[:3]) + (values[0]*values[2]*values[3]),
            (values[0]*values[1]*values[3]) + math.prod(values[1:]))

        N=M
        dp=[[0 for _ in range(N)] for _ in range(M)]
        dp[M-3][-1]=math.prod(values[-3:])

        for m in range(M-4,-1,-1):
            stage_m=dp[m]

            for s_m in range(m+2,N):
                if s_m==m+2:
                    stage_m[s_m]=values[m]*values[m+1]*values[m+2]
                    continue
                else:
                    F=[]
                    F.append(values[m]*values[m+1]*values[s_m] + dp[m+1][s_m])
                    for x_m in range(m+2,s_m-1):
                        F.append(dp[m][x_m]+dp[x_m][s_m] + values[m]*values[x_m]*values[s_m])
                    F.append(dp[m][s_m-1]+values[s_m-1]*values[s_m]*values[m])
                    stage_m[s_m]=min(F)

        return dp[0][-1]
                


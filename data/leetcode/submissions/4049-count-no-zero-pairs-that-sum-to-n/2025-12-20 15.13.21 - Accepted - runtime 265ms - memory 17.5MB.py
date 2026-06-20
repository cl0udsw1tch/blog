class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        '''
        carry_m: carry bit
        endedA_m: a has ended (MSD)
        endedB_m: b has ended (MSD) 
        ''' 
        str_n=str(n)
        arr_n=[int(c) for c in str_n][::-1]
        M=len(arr_n)

        dp=[[[[0,0] for endedA_m in range(2)] for carry_m in range(2)] for m in range(M)]

        num=arr_n[0]
        stage_m=dp[0]
        for x1 in range(1, 10):
            for x2 in range(1, 10):
                if (x1+x2)%10 != num: continue
                carry_m=int(x1+x2>9)
                stage_m[carry_m][0][0]+=1

        for m in range(1, M):
            stage_m=dp[m]
            stage_mm1=dp[m-1]
            num=arr_n[m]
            for carry_mm1 in [0,1]:
                for endedA_mm1 in [0,1]:
                    for endedB_mm1 in [0,1]:
                        for x1 in range(0, 10):
                            for x2 in range(0, 10):
                                if (x1+x2+carry_mm1)%10 != num: continue
                                if (endedA_mm1 and x1) or (endedB_mm1 and x2): continue
                                carry_m=int(x1+x2+carry_mm1>9)
                                endedA_m=int(endedA_mm1 or x1==0)
                                endedB_m=int(endedB_mm1 or x2==0)
                                f=stage_mm1[carry_mm1][endedA_mm1][endedB_mm1]
                                stage_m[carry_m][endedA_m][endedB_m]+=f

        return sum([dp[M-1][0][j][k] for j in range(2) for k in range(2)])
                    





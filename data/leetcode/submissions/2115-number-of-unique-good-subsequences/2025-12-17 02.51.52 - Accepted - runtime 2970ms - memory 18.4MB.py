class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        '''
        f*_m(s_m) returns number of unique good subsequences in binary[:m+1] ending in s_m

        '''
        if len(binary)==1: return 1

        if '1' not in binary: return 1

        hasZero=0
        if '0' in binary: hasZero=1

        firstOne=binary.index("1")
        binary=binary[firstOne:]
        M=len(binary)

        dp=[[0,0] for _ in range(4)] 
        dp[2]=[0,1]

        chars=["0", "1"]
        for m in range(1,M):
            stage_m=dp[3]
            stage_mp1=dp[2]
            
            for s_m in [0,1]:
                ss_m=chars[s_m]
                stage_prev=dp[s_m]

                F=[0,0]
                for x_m in ['take_prev', 'make_new']:
                    if x_m=='take_prev':
                        f=stage_mp1[s_m]
                        F[0]=f
                    else:
                        f=stage_mp1[0] + stage_mp1[1] - (stage_prev[0] + stage_prev[1])
                        if binary[m]==ss_m:
                            F[1]=f
                f_sum=sum(F)
                stage_m[s_m]=f_sum
            
            dp[0]=stage_mp1 if binary[m]=="0" else dp[0]
            dp[1]=stage_mp1 if binary[m]=="1" else dp[1]
            dp[2]=stage_m
            dp[3]=[0,0]

        MOD=10**9+7
        return (dp[2][0] + dp[2][1] + hasZero) % MOD

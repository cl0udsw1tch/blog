class Solution:
    def minCut(self, s: str) -> int:
        '''
        aa b (1)
        a a b (2)
        a 
        '''
        M=len(s)
        if M==1:
            return 0
        if M==2:
            return int(s[0]!=s[1])

        palindromeMap=[[False for _ in range(M)] for _ in range(M)]
        palindromeMap[-1][-1]=True
        for m in range(M-2,-1,-1):
            stage_m=palindromeMap[m]
            for s_m in range(m, M):
                F=False
                if m==s_m:
                    F=True
                elif s_m==m+1 and s[m]==s[s_m]:
                    F=True
                elif s[m]==s[s_m] and palindromeMap[m+1][s_m-1]:
                    F=True
                stage_m[s_m]=F

        
        dp=[[float('inf')] for _ in range(M)]
        dp[-1][0]=0
        
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            s_m=0
            F=[float('inf')]
            if palindromeMap[m][M-1]:
                stage_m[s_m]=0
                continue
            for x_m in range(m,M-1):
                if not palindromeMap[m][x_m]:continue
                f=1 + dp[x_m+1][0]
                F.append(f)
            f_min=min(F)
            stage_m[s_m]=f_min
        return dp[0][0]
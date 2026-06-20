class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) gives whether or not s[m:s_m] is a palindrome
        '''

        M=len(s)
        N=len(s)
        if M==1:
            return s[0]
        if M==2:
            return s if s[0]==s[1] else s[0]
        
        dp=[[False for _ in range(N)] for _ in range(M)]
        dp[-1][-1]=True

        for m in range(M-2,-1,-1):

            stage_m=dp[m]
    
            for s_m in range(m, N):
                F=False
                if m==s_m:
                    F=True
                elif s_m==m+1 and s[m]==s[s_m]:
                    F=True
                elif s[m]==s[s_m] and dp[m+1][s_m-1]:
                    F=True
                stage_m[s_m]=F

        

        t=[[(m,n) for n in range(N) if dp[m][n]] for m in range(M)]
        t1,t2=max([max(row, key=lambda x: x[1]-x[0]+1) for row in t], key = lambda x: x[1]-x[0]+1)
        r=s[t1:t2+1]
        return r


                

      
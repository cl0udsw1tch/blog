class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        stage_n: n=0...n-1 subproblem solves the problem for s[n:N]
        s_n: current index
        x_n: length of substring to encode starting at s_n
            => s_n + x_n = s_{n'}
        f_n(s_n, x_n) = f*_n'(s_n') if s[s_n:s_n+x_n] is valid, else 0 
        f*_n(s_n) = \sum (f*_n'(s_n'))

        '''

        N=len(s)
        if N==1:
            return int(s[0] != "0")
        if N==2:
            if s[0]=="0": return 0
            if s[1]=="0" and int(s) < 26: return 1
            if int(s)<=26: return 2



        dp=[[0] for _ in range(N)]

        n=N-1
        stage_n=dp[n]
        if s[n]!="0":
            stage_n[0]=1

        n=N-2
        stage_n=dp[n]
        F=[int(s[n]!="0")*dp[n+1][0], int(s[n]!="0" and int(s[n:])<=26)]
        stage_n[0]=sum(F)

        for n in range(N-3,-1,-1):
            stage_n=dp[n]
            s_n=n
            F=[0,0]
            x_n=1
            substr=s[s_n:s_n+x_n]
            f = int(substr[0]!="0") * dp[s_n+x_n][0]
            F[0]=f
            x_n=2
            substr=s[s_n:s_n+x_n]
            f = int(substr[0] != "0" and int(substr)<=26) * dp[s_n+x_n][0]
            F[1]=f
            f_sum = sum(F)
            stage_n[0]=f_sum
        return dp[0][0]

                
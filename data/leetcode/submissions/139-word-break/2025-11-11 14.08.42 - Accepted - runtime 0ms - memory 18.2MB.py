class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        stage_n: n=0...N-1 suproblem solves the problem for s[n:N]
        s_n: current char index
        x_n: where to make the next cut
            => s_{n'}=x_n
        f_n(s_n,x_n) = s[s_n:x_n] \in wordDict AND f*_{n'}(s_{n'})
        f*_n(s_n)= ANY_{x_n}(f_n(s_n,x_n))
        '''
        N=len(s)
        L=len(max(wordDict, key = lambda x: len(x)))
   
        wordDict=dict.fromkeys(wordDict)
        if N==1: return s in wordDict

        dp=[[False] for _ in range(N)]
        dp[N-1][0]=s[-1] in wordDict

        for n in range(N-2,-1,-1):
            stage_n=dp[n]
            s_n=n
            if s[s_n:N] in wordDict:
                stage_n[0]=True
                continue
            if s_n+L<N and s[s_n:s_n+L] in wordDict and dp[s_n+L][0]:
                stage_n[0]=True
                continue
            
            f_any=False
            for x_n in range(s_n+1, min(s_n+L,N)):
                stage_s_np = dp[x_n]
                f=(s[s_n:x_n] in wordDict) and stage_s_np[0]
                if f:
                    f_any=True
                    break
        
            stage_n[0]=f_any

        return dp[0][0]
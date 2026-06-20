class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        stage_n: n=0...N-1 subproblem solves the problem for pairs[n...N-1]
        s_n: current index
        x_n: next pair 
            => s_n'=x_n
        f_n(s_n,x_n) = 1 + f*_n'(s_n')
        f*_n(s_n) = max(f_n(s_n,x_n))
        '''

        N=len(pairs)
        if N==1: return 1
        pairs.sort(key=lambda pair: pair[0])
        dp=[[1] for _ in range(N)]

        for n in range(N-2,-1,-1):
            s_n=n
            pair_n=pairs[n]
            stage_n=dp[n]
            F=[1 for _ in range(n,N)]

            for x_n in range(n+1,N):
                s_np1=x_n
                pair_np1=pairs[s_np1]
                stage_np1=dp[s_np1]
                if not pair_np1[0] > pair_n[1]: continue
                F[x_n-n]=1+stage_np1[0]

            f_max=max(F)
            stage_n[0]=f_max
        return max(dp, key = lambda stage: stage[0])[0]

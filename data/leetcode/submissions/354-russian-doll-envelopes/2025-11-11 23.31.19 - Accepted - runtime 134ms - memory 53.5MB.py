from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        stage_n: n=0...N-1 subproblem solves the problem for envelopes[n...N-1]
        s_n: current index
        x_n: index of next envelope to fit inside envelope at s_n
            => s_n' = x_n
        f_n(s_n,x_n) = 1 + f*_n'(s_n')
        f*_n(s_n) = max_{x_n}(f_n(s_n,x_n))
        
        N=len(envelopes)
        if N == 1: return 1

        sorted_envs=sorted(envelopes, key=lambda x : x[0], reverse=True)

        dp = [[1] for _ in range(N)]
        for n in range(N-2,-1,-1):
            stage_n=dp[n]
            s_n=n
            env_n = sorted_envs[s_n]
            F=[1 for _ in range(n, N)]

            for x_n in range(n+1, N):
                s_np1=x_n
                env_np1=sorted_envs[s_np1]
                if (not (env_np1[0] <  env_n[0])) or (not (env_np1[1] < env_n[1])):
                    continue
                stage_np1=dp[s_np1]
                F[x_n-n]=1+stage_np1[0]
                
            f_max=max(F)
            stage_n[0]=f_max
        return max(dp, key=lambda stage : stage[0])[0]
        '''
        sorted_envs=sorted(envelopes, key=lambda x : (x[0],-x[1]))

        T=[]
        H=[env[1] for env in sorted_envs]
        for h in H:
            i = bisect_left(T,h)
            if i == len(T):
                T.append(h)
            else:
                T[i]=h
        return len(T) 



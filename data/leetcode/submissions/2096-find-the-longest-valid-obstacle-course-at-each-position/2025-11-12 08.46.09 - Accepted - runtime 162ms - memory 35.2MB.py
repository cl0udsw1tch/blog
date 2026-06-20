from bisect import bisect_left
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        '''
        stage_n: n=0...n-1 subproblem solves the problem for obstacles[0...n]
        s_n: current index
        x_n: index of next element
            s_n'=x_n
        f_n(s_n, x_n) = 1 + f*_n'(s_n')


        N=len(obstacles)
        if N == 1: return [1]

        dp=[1 for _ in range(N)]

        for n in range(1,N):
            s_n=n
            obs_n=obstacles[n]
            F=[1 for _ in range(0, n+1)]
            for x_n in range(0,n):
                s_np1=x_n
                obs_np1=obstacles[s_np1]
                if not obs_n >=obs_np1: continue
                F[x_n]=1+dp[s_np1]
            f_max=max(F)
            dp[n]=f_max
        return dp
        '''
        N=len(obstacles)
        if N == 1: return [1]
        dp=[1 for _ in range(N)]
        T=[obstacles[0]]
        for j,obs in enumerate(obstacles[1:N]):
            i=bisect_right(T, obs)
            if i==len(T):
                T.append(obs)
            else:
                T[i]=obs
            dp[j+1]=i+1
        return dp


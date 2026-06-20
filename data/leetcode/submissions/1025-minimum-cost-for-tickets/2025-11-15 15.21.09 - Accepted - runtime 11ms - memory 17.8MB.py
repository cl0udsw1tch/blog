from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        stage_n: n=[days[0],days[N-1]] solves the subproblem f*_n() for days[n]..days[n]+1...days[N] 
        s_n: {n}
        x_n: the ticket bought on day_n=day[n]
        => s_n' = s_n+duration(x_n)
        f_n(s_n, x_n) = cost[x_n] + f*_n'(s_n') 
        f*_n(s_n) = min(f_n(s_n,x_n))

        '''

        S=days[0]
        E=days[-1]
        D=E-S
        N=len(days)
        if N==1:
            return min(costs)
        
        dp=[ [0] for _ in range(D+2) ]
        durations=[1,7,30]

        for n in range(D,-1,-1):
            d_n=S+n
            F=[0 for _ in range(3)]
            for x_n in range(3):
                duration = durations[x_n]
                ticket_cost = costs[x_n]
                d_np = bisect_left(days, d_n+duration)
                np=(days[d_np] if d_np<N else days[-1]+1)-S
                F[x_n] = ticket_cost + dp[np][0]
            dp[n][0] = min(F)

        return dp[0][0]
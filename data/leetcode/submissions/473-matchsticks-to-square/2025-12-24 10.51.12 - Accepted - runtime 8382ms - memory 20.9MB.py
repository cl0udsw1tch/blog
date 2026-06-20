class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        N=len(matchsticks)
        if N<4: return False

        S=sum(matchsticks)
        M=4

        memo={}
        memo[(M, (2**N-1))]=True

        isQuarterLen=[False]* (2**N)
        for x in range(2**N):
            matches=[j for j in range(N) if (x>>j)&1] # can be precomputed
            isQuarterLen[x]= sum([matchsticks[i] for i in matches]) == S//4
        X=[i for i in range(2**N) if isQuarterLen[i]]

        def dfs(s):
            if s in memo: return
            sidesDone, mask=s
            if sidesDone==M:
                memo[s]=mask==2**N-1
            
            F=False
            for x in X:
                if x & mask: continue

                s_p=sidesDone+1, mask | x
                dfs(s_p)

                F=F or memo[s_p]
                if F: break

            memo[s]=F
        
        dfs((0,0))
        return memo[(0,0)]

            
            

            


            

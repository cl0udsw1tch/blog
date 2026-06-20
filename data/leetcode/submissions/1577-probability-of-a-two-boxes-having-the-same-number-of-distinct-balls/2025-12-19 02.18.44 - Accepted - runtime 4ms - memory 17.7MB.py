class Solution:
    def getProbability(self, balls: List[int]) -> float:
        M=len(balls)
        S=sum(balls)
        N=S//2
        if S==2:
            return 1


        memo={}
        def dfs(s):
            if s in memo: return
            m,sz1,sz2,d1,d2=s
            if m==M:
                memo[s]=int(d1==d2), 1
                return
            
            feasible_low=max(0,balls[m]-(N-sz2))
            feasible_high=min(balls[m],N-sz1)
            F=[0]*(feasible_high+1-feasible_low)
            for x in range(feasible_low, feasible_high+1):
                s_p=m+1,sz1+x,sz2+balls[m]-x,d1+int(x>0),d2+int(balls[m]-x>0)
                dfs(s_p)
                c=math.comb(balls[m], x)
                f=c*memo[s_p][0], c*memo[s_p][1] #quotient space against permutations
                F[x-feasible_low]=f
            memo[s]=sum([f[0] for f in F]), sum([f[1] for f in F])
        dfs((0,0,0,0,0))
        q=memo[(0,0,0,0,0)]
        return q[0]/q[1]
                
                    



            
            




class Solution:
    def soupServings(self, n: int) -> float:
        if n>10000: return 1
        memo={}
        X=[(-100, 0), (-75, -25), (-50, -50), (-25,-75)]
        def dfs(s):
            if s in memo: return

            v,w = s
            if v<=0 and w>0:
                memo[s]=(1,0)
                return
            if v<=0 and w<=0:
                memo[s]=(0,1)
                return
            if v>0 and w<=0:
                memo[s]=(0,0)
                return

            F=[(0,0)]*4
            c=0
            for x in X:
                s_p=(s[0]+x[0], s[1]+x[1])
                dfs(s_p)
                f=(1/4) * memo[s_p][0], (1/4) * memo[s_p][1]
                F[c]=f
                c+=1
            memo[s]=(sum([f[0] for f in F]), sum([f[1] for f in F]))
        dfs((n,n))
        return memo[(n,n)][0] + (1/2)*memo[(n,n)][1]

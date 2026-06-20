class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        M=len(words)
        if M==1: return words[0]
        
        def cost(a, b):
            max_overlap=0
            i=0
            while i < min(len(words[a]), len(words[b])):
                if words[a][-1-i:] == words[b][:i+1]:
                    max_overlap=i+1
                i+=1
            return len(words[b]) - max_overlap

        cost_memo={}
        dp=[[[(float('inf'),-1) for _ in range(M)] for _ in range(1<<M)] for _ in range(M)]
        dp[-1]=[[(0,-1) for _ in range(M)] for _ in range(1<<M)]

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            for s_m in range(1<<M): # mask
                if s_m.bit_count() != m+1: continue
                for t_m in range(M): # current city
                    if not ((1<<t_m)&s_m): continue
                    F=[(float('inf'),-1)]*M
                    for x_m in range(M): # next city
                        if (1<<x_m) & s_m: continue
                        c=0
                        if (t_m, x_m) in cost_memo:
                            c=cost_memo[(t_m, x_m)]
                        else:
                            c=cost(t_m, x_m)
                            cost_memo[(t_m, x_m)]=c

                        f = c + stage_mp1[s_m | (1<<x_m)][x_m][0]
                        F[x_m]=(f,x_m)
                    f_min, x_m_star=min(F, key=lambda x: x[0])
                    stage_m[s_m][t_m]=(f_min, x_m_star)
                   
        min_t_ms=[(s_m,min(enumerate(dp[0][s_m]), key=lambda x: len(words[x[0]])+x[1][0])[0]) for s_m in range(1<<M)]
        min_t_m=min(min_t_ms, key=lambda x: len(words[x[1]])+dp[0][x[0]][x[1]][0])
        path=[(min_t_m[0], min_t_m[1], 0)] # mask, curr, cost
        m=0
        while m<M-1:
            last=path[-1]
            s_m, t_m=last[0], last[1]
            val=dp[m][s_m][t_m]
            cost, x_m=val
            s_mp1, t_mp1=s_m | (1<<x_m), x_m
            path.append((s_mp1, t_mp1, cost))
            m+=1
            
        r=words[path[0][1]]
        for step in range(1,M):
            prev=path[step-1][1]
            curr,cost=path[step][1], path[step][2]-(path[step+1][2] if step+1<M else 0)
            r+=words[curr][-cost:]
        return r


                 
            
            
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        M=len(s)
        if M==1: return 1
        
        memo={}
        memo[M]=1

        def dfs(t):
            if t in memo:
                return
            
            letter=s[t]

            F=[0,0]

            t_p=t+1
            dfs(t_p)
            F[0]=memo[t_p] #skip

            if letter in s[t_p:]: #take
                j=s.index(letter, t_p)
                F[1]=memo[t_p]-memo[j+1]
            else:
                F[1]=memo[t_p]
            
            f_sum=sum(F)
            memo[t]=f_sum

        dfs(0)
        return (memo[0]-1) % (10**9 + 7)

                
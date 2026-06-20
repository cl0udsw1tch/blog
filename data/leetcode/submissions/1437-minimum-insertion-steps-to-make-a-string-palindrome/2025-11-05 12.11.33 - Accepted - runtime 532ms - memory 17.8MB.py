class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        stage_n: 0...N-1
        s_n: the stage-n+1 size substring to compute how many steps are needed to turn into a palindrome
            => particularly, s_n is the index of the start of the substring
        x_n: the index a char is being inserted at (front or back), or an empty character ""
            => if a character is inserted at 0, then s_{n+1} = s_n[1:n]
            => if a character is inserted at n, then s_{n+1} = s_n[0:n-1]
        f_n(s_n, x_n) = cost(x_n) + f*_n(s_{n+1}) where cost(x_n) = 1 if x_n is an insertion, 0 elsewise
        f*_n(s_n) = min_{x_n} {f_n(s_n,x_n)} is the optimal cost when x*_n is taken, that is an insertion at one end
        or no character inserted


        '''
        N=len(s)
        if N==1:
            return 0
        if N==2:
            return int(s[0]!=s[1])
        if N==3:
            return int(s[0]!=s[2])

            
        dp=[[], [], [0]*N]
        stage_n=dp[1]
        stage_np1=dp[2]
        for s_n in range(N-1):
            ss_n=s[s_n:s_n+2]
            if ss_n[0]==ss_n[-1]:
                stage_n.append(0)
            else:
                stage_n.append(1)

        for n in range(3, N+1):
            stage_n=dp[0]
            stage_np1=dp[1]
            stage_np2=dp[2]

            for s_n in range(N-n+1):
                ss_n=s[s_n:s_n+n]
                f_star=0
                F=[]
                if ss_n[0]==ss_n[-1]:
                    s_np2=s_n+1
                    f_star=0+stage_np2[s_np2]
                else:
                    s_np1=[s_n, s_n+1]
                    f_star=1+min([stage_np1[s_np1[0]], stage_np1[s_np1[1]]])
                stage_n.append(f_star)

            dp[2]=stage_np1
            dp[1]=stage_n
            dp[0]=[]
   
        return min(dp[1])




        
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        '''
        stage_n subproblem: n = 0...N-1 how many jumps left to termial index. The subprblm solution is
                            finding all states that give n jumps
        s_n: all possible indices n jumps away from terminal
        x_n: all possible directions to a next index from a given s_n, or possibly no jump at all
        f_n(s_n, x_n) = 1(if jump else 0) + f*_{n+1}(s_n) for all valid pairs (s_n, x_n)
        f*_n(s_n) = max_{x_n} {f_n(s_n, x_n)}
        '''   
        N = len(arr)
        if N==1:
            return 1
        if N==2:
            return 2

        dp=[[1 for _ in range(N)]]
        sortedArr = sorted(enumerate(arr), key=lambda x:x[1])
        dp[0][sortedArr[0][0]]=1

        for n in range(1,N):
            stage_n=dp[0]
            stage_np1=dp[0]
            s_n=sortedArr[n][0]
            F=[stage_np1[s_n]]
            for s_np1 in range(s_n-1,max(-1,s_n-d-1),-1):
                if arr[s_np1]>=arr[s_n]:
                    break
                else:
                    F.append(stage_np1[s_np1]+1)
            for s_np1 in range(s_n+1, min(N,s_n+d+1)):
                if arr[s_np1]>=arr[s_n]:
                    break
                else:
                    F.append(stage_np1[s_np1]+1)
            f_max=max(F)
            stage_n[s_n]=f_max
 
        r=max(dp[0])
        print(r)
        return r


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        '''
        stage_n: what row we're on
        s_n: position (i, j)
        x_n: left, up, or upleft {(0,-1), (-1, 0), (-1,-1)} some number of times until next row reached OR end 'E' 
        is reached
        f_n(s_n, x_n): cost of being at pos s_n, moving x_n, and making max cost decisions after to maximize cost
            => f_n(s_n, x_n) = cost(s_n) + f*_{n+1}(s_np1 = s_n + x_n)
        f*_n(s_n) = cost(s_n) + max_{x_n} f*_{n+1}(s_n + x_n)

        many unfeasable paths, so bottom-up

        '''
        
        N=len(board)
        dp=[[],[]]
        dupes=[[1]*N for n in range(N)]
        dupes[0]=[1]*N

        for c in board[0]:
            if c=="E":
                dp[1].append(0)
            elif c=="X":
                dp[1].append(-math.inf)
            else:
                dp[1].append(int(c)+dp[1][-1])

        for n in range(1, N):
            stage_n=dp[0]
            stage_np1=dp[1]
            row_n=board[n]
            row_np1=board[n-1]
            firstObs=-1
            if n==N-1:
                firstObs=row_n.rfind("X")
                if firstObs!=-1:
                    for s_n in range(firstObs+1):
                        stage_n.append(-math.inf)
            for s_n in list(range(N))[firstObs if firstObs!=-1 else 0:N]:
                f_star=[-math.inf, 0]
                for x_n in range(s_n+1):
                    f=0
                    for c in row_n[x_n:s_n+1][::-1]:
                        if c == "X":
                            f+=-math.inf
                            break
                        elif c=="S":
                            f+=0
                        else:
                            f+=int(c)
                    d=1
                    if x_n==0 or stage_np1[x_n] > stage_np1[x_n-1]:
                        f+=stage_np1[x_n]
                        d*=dupes[n-1][x_n]
                    else:
                        f+=stage_np1[x_n-1]
                        d*=dupes[n-1][x_n-1]
                    if f > f_star[0]:
                        f_star = [f, d]
                    elif f==f_star[0]:
                        f_star[1]+=d

                dupes[n][s_n]=f_star[1]%(10**9 + 7)
                stage_n.append(f_star[0])

            dp[1]=stage_n
            dp[0]=[]

        r=max(dp[1])
        if r == -math.inf:
            return [0,0]
        return([r, dupes[N-1][N-1]])




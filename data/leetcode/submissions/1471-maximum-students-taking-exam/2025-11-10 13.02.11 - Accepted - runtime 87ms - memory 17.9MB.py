class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        '''
        stage_n: for n=1..N, the subproblem considers the optimal arrangement for rows [n..N]
        s_n: all possible seating arrangements for the current row (bitmask)
        x_n: all possible seating arrangements for the row below (bitmask)
            => x_n=s_{n+1}
        f_n(s_n,x_n) = sum of seats of current row + optimal sum for rows below
                    = sum(s_n) + f*_{n+1}(s_{n+1})
        f*_n(s_n) = max(f_n(s_n, x_n))

        '''
        R=len(seats)
        C=len(seats[0])
        arr2int= lambda arr: int("".join(map(str,arr)), 2)
        seats_n=seats[-1]
        C_n=sum([1 if seat=="." else 0 for seat in seats_n])
        
        dp=[[], [1 for _ in range(2**C_n)]]
        
        for s_n in range(2**C_n):
            s_n_mask=[(s_n >> j) & 1 for j in range(C_n)]
            s_n_seats_mask=[0 for _ in range(C)]
            i=0
            for j in range(C):
                if seats_n[j]==".":
                    s_n_seats_mask[j]=s_n_mask[i]
                    i+=1
            s_n_seats_mask_int=arr2int(s_n_seats_mask)
            if s_n_seats_mask_int&(s_n_seats_mask_int>>1):
                dp[1][s_n]=(-math.inf, s_n_seats_mask_int)
            else:
                dp[1][s_n]=(sum(s_n_mask), s_n_seats_mask_int)
    
        for n in range(R-2,-1,-1):
            seats_n=seats[n]
            C_n=sum([1 if seat=="." else 0 for seat in seats_n])
            dp[0]=[1 for _ in range(2**C_n)]
            stage_n=dp[0]
            stage_np1=dp[1]
            for s_n in range(2**C_n):
                F=[-math.inf for _ in range(len(stage_np1))]
                s_n_mask=[(s_n >> j) & 1 for j in range(C_n)]
                s_n_seats_mask=[0 for _ in range(C)]
                i=0
                for j in range(C):
                    if seats_n[j]==".":
                        s_n_seats_mask[j]=s_n_mask[i]
                        i+=1

                s_n_seats_mask_int=arr2int(s_n_seats_mask)

                if s_n_seats_mask_int&(s_n_seats_mask_int>>1):
                    stage_n[s_n]=(-math.inf, s_n_seats_mask_int)
                else:
                    for s_np1 in range(len(stage_np1)):
                        f, s_np1_seats_mask_int=stage_np1[s_np1]
                        if s_n_seats_mask_int&(s_np1_seats_mask_int>>1) | \
                            s_n_seats_mask_int&(s_np1_seats_mask_int<<1):
                            F[s_np1]=-math.inf
                        else:
                            F[s_np1]=f+sum(s_n_mask)
                    f_max=max(F)
                    stage_n[s_n]=(f_max,s_n_seats_mask_int)
            dp[1]=stage_n

        r= max(dp[1], key=lambda x: x[0])[0]
        print(r)
        return(r)



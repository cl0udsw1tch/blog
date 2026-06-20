class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        **********************************************************************************************************
        each operation involves two elements, with created ones being descendents of only ONE of the elements in an 
        operation (since the other operand disappears, that is, y-x is a descendent of y, not x since it gets 
        destroyed), thus we can split the elements so that each element belongs to one of two sets A_0 and B_0,
        which after some i number of reductions transforms to A_i, B_i where each set contains descendents of its
        original in A_{i-1} and B_{i-1} respectively. Then since an op either decreases both sets by 

        * x=y       (when they are equal) or by 
        * min(x,y)  (max(x,y) becomes max(x,y)-min(x,y) and the other min(x,y) becomes 0 = min(x,y)-min(x,y)), 
        
        => **the sets decrease by the same amount** after every op (as i increments) and the difference 
        sum(A_i)-sum(B_i) will always be fixed, and so will abs(sum(A_i)-sum(B_i)). 
        By the end, since only 1 element can remain, one of A or B must eventually become empty, thus sum(A)-sum(B)
        will give += the last element, and thus abs(sum(A)-sum(B)) will give the last element (or both empty and 
        this returns 0 as needed). Thus to find the least result, abs(sum(A)-sum(B)) must me minimized. 
        
        Ex) [1,2,3,5,5,4,1]
        * ___: A_0 = [1,2,3,4]    B_0 = [5,5,1]     => |A|=10,  |B|=11
        * op1: A_1 = [1,2,3,_]    B_1 = [1,5,1]     => |A|=6,   |B|=7 
        * op2: A_2 = [_,2,3,_]    B_2 = [_,5,1]     => |A|=5,   |B|=6
        * op3: A_3 = [_,_,3,_]    B_3 = [_,3,1]     => |A|=3,   |B|=4
        * op4: A_4 = [_,_,_,_]    B_4 = [_,_,1]     => |A|=0,   |B|=1
        so the result R = abs(|A|-|B|)

        Then all that needs to be found is the largest A : |A| <= sum(stones)/2, i.e the largest subset A
        with sum as closest to half the sum of the total set, since then

        R = |B|-|A|
          = (sum(stones) - |A|) - |A|  
          = sum(stones) - 2|A|

        *************************************************************************************************************
        stage_n: n=0...N-1 subproblem solves the problem for stones[n..N] and possible total sums for this collection
            => dp[n][i] = boolean(possible to make weight i with stones[n...N])
        s_n: = 0... S/2
        x_n: keeping or ignoring stones[n]
            => stones[n] stays:     x_n = -stones[n]    => s_{n+1} = s_n - stones[n]
            => stones[n] dismissed: x_n = 0             => s_{n+1} = s_n
            => s_{n+1} = s_n+x_n
        f_n(s_n, x_n) = f*_{n+1}(s_{n+1})
        f*_n(s_n) = ANY_{x_n} (f_n(s_n, x_n))
        '''

        N=len(stones)
        if N==1:
            return stones[0]
        total=sum(stones)
        S=total >> 1

        dp=[[], [False for _ in range(0, S+1)]]
        dp[-1][0]=True
 
        for n in range(N-1,-1,-1):
            stage_n=[False for _ in range(0, S+1)]
            stage_np1=dp[1]
            stone_n=stones[n]

            for s_n in range(0, S+1):
                F=[False, False]
                x_n=0
                s_np1=s_n+x_n
                f=stage_np1[s_np1]
                F[0]=f
                if s_n >= stone_n:
                    x_n=-stone_n
                    s_np1=s_n+x_n
                    f=stage_np1[s_np1]
                    F[1]=f
                f_any=any(F)
                stage_n[s_n]=f_any
            dp[1]=stage_n
        
        return total - 2 * (S-dp[1][::-1].index(True))



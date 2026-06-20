
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        stage_n: n = 0...N-1 subproblem finds f_n*(i) = nums[n...N] has a subset of sum i = 0...sum(nums) // 2
        s_n: all possible sums for the smaller partition = 0...sum(nums) // 2
        x_n: whether to include nums[n] or skip nums[n]
            => include: x_n = -nums[n] => s_{n+1} = s_n - nums[n]
            => skip   : x_n = 0        => s_{n+1} = s_n
            => s_{n+1} = s_n + x_n
        f_n(s_n, x_n) = f*_{n+1}(s_{n+1})
        f*_n(s_n) = ANY_{x_n} (f_n(s_n, x_n))

        
        N=len(nums)
        if N==1: return nums[1]
        if N==2: return abs(nums[0]-nums[1])
        nums.sort()
        if nums[0] < 0:
            nums=[num-nums[0]+1 for num in nums]

        sums=[0 for _ in range(2**N)]
        sums[-2:]=[nums[-1],0]
        for i in range(1,N):
            sums[-2**(i+1):-2**(i)]=[a + nums[N-1-i] for a in sums[-2**(i):]]
        sums.sort(reverse=True)
        sumidxs={a:i for i,a in enumerate(sums)}

        T=sum(nums)
        H=T>>1
        P=len(sums)
        M=N>>1
        dp = [[[False for _ in range(M+1)] for _ in range(P)]] #(n=N)
        dp[0][sumidxs[0]][0]=True

        for n in range(N-1,-1,-1):
            stage_n=[[False for _ in range(M+1)] for _ in range(P)]
            stage_np1=dp[0]
            num_n=nums[n]
            for i in sums:
                for j in range(0, M+1):
                    s_n=(i,j)
                    F=[False, False]
                    x_n=(0,0)
                    s_np1=s_n[0]+x_n[0], s_n[1]+x_n[1]
                    if sumidxs.get(s_np1[0], None) is not None:
                        f=stage_np1[sumidxs[s_np1[0]]][s_np1[1]]
                        F[0]=f
                    if s_n[0]>=num_n and s_n[1]>=1:
                        x_n=(-num_n, -1)
                        s_np1=s_n[0]+x_n[0], s_n[1]+x_n[1]
                        if sumidxs.get(s_np1[0], None) is not None:
                            f=stage_np1[sumidxs[s_np1[0]]][s_np1[1]]
                            F[1]=f
                    f_any=any(F)
                    stage_n[sumidxs[s_n[0]]][s_n[1]]=f_any
            dp[0]=stage_n

        closestSum=-math.inf
        for j in range(P-1, -1, -1):
            if sums[j]>H: break
            if dp[0][j][M]: closestSum=sums[j]
        r = T - 2 * closestSum
        return r
        

        '''
        N=len(nums)
        if N==1: return nums[1]
        if N==2: return abs(nums[0]-nums[1])
        nums.sort()
        if nums[0]<0:
            nums=[num-nums[0]+1 for num in nums]
        T=sum(nums)
        H,M =T>>1,N>>1
        A,B=nums[:M], nums[M:]

        A_sums,B_sums = [0 for _ in range(2**M)], [0 for _ in range(2**M)]
        A_sums[-2:],B_sums[-2:] = [(1,A[-1]),(0,0)],[(1,B[-1]),(0,0)]
        for i in range(1,M):
            A_sums[-2**(i+1):-2**(i)]=[(1+a[0], a[1] + A[M-1-i]) for a in A_sums[-2**(i):]]
            B_sums[-2**(i+1):-2**(i)]=[(1+a[0],a[1] + B[M-1-i]) for a in B_sums[-2**(i):]]

        A_sums.sort(),B_sums.sort()

        r=math.inf
        for a_len, a_sum in A_sums:
            if a_sum>H: continue

            b_target=(M-a_len, H-a_sum)
            i = bisect_left(B_sums, b_target)
            if i == len(B_sums): continue
            if B_sums[i]==b_target:
                closest_sum=B_sums[i][1]
                return T - 2*(a_sum + closest_sum)
            if B_sums[i-1][0] < b_target[0]: continue

            closest_sum=B_sums[i-1][1]
            r=min(r, T - 2*(a_sum + closest_sum))

        return r

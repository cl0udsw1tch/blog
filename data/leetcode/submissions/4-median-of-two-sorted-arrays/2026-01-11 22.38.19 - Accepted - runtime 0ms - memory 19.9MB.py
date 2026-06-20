class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        '''
        A=[1,13,20,40] B=[2,5,17,28] left_n=4
        
        i=0,j=4 => f(i) = max(A[-1],B[3]) - min(A[0], B[4]) = max(-inf, 28)-min(1,inf)=28-1>0
        i=1,j=3 => f(i) = max(A[0], B[2]) - min(A[1], B[3]) = max(1,17)-min(13,28)=17-13>0
        i=2,j=2 => f(i) = max(A[1], B[1]) - min(A[2], B[2]) = max(13,5)-min(20,17)=13-17<0
        i=3,j=1 => f(i) = max(A[2], B[0]) - min(A[3], B[1]) = max(20,2)-min(40,5)=20-5>0
        i=4,j=0 => f(i) = max(A[3], B[-1])- min(A[4], B[0]) = max(40,-inf)-min(inf,2)=40-2>0

        f(i) isnt monotone :( however f(i=0..4) = [27,4,-4,15,38], which is decreasing 
        and then increasing after it dips below 0 ONCE, so the DERIVATIVE is monotone 

        SENTINELS: f(max(0,left_n-N)-1) = inf = f(min(M, left_n)+1)
        => in this ex: f(-1) = inf = f(5)

        g(i):= f(i)-f(i-1)
        => g(1...4)=[-23,-8,19,23]
        => SENTINELS: g(max(0,left_n-N)-1) = -inf, g(min(M, left_n)+1)=inf
        P(i) := g(i) <= 0 THIS IS THE TRUE MONOTONE PREDICATE WOOHOOOOOOOO!!!! 

        '''
        M,N=len(nums1),len(nums2)
        if M==0: return nums2[N//2] if N%2 else (nums2[N//2-1]+nums2[N//2])/2
        if N==0: return nums1[M//2] if M%2 else (nums1[M//2-1]+nums1[M//2])/2
        if M==1 and N==1: return (nums1[0]+nums2[0])/2
        
        left_n=ceil((M+N)/2)
   
        f = lambda i,j: max(get(nums1,i-1), get(nums2,j-1))-min(get(nums1,i), get(nums2,j))

        def g(i1,j1,i2,j2):
            f_i = f(i1,j1) if i1<M+1 else float('inf')
            f_prev = f(i2,j2) if i2>max(0,left_n-N)-1 else float('inf')
            return f_i-f_prev
        
        P=lambda i1,j1,i2,j2 : g(i1,j1,i2,j2) <= 0
        phi=lambda i : (i,left_n-i,i-1,left_n-i+1)
        P_phi=lambda i : P(*phi(i))

        l,r=max(0,left_n-N)-1,min(M, left_n)+1
        while l+1<r:
            MID=(l+r)//2
            if P_phi(MID):
                l=MID
            else:
                r=MID

        i,j=l,left_n-l
        if (M+N)%2==0:
            return (max(get(nums1,i-1),get(nums2,j-1))+min(get(nums1,i),get(nums2,j)))/2
        else:
            return max(get(nums1,i-1),get(nums2,j-1))

def get(arr, i):
    M=len(arr)
    if i<0: return -float('inf')
    if i>M-1: return float('inf')
    return arr[i]
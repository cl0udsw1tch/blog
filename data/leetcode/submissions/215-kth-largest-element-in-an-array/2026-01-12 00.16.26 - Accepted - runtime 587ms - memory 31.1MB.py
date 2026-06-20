class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        M=len(nums)
        if M==1: return nums[0]

        SENTINEL=-float('inf')
        heap=[0]*(M+1)
        heap[0]=SENTINEL
        count=0

        for num in nums:
            count+=1
            heap[count]=num   
            n=count
            while heap[n]<heap[n//2] and n//2>0:
                heap[n],heap[n//2]=heap[n//2],heap[n]
                n=n//2

        curr=None
        for j in range(M-k+1):
            curr=heap[1]
            heap[1]=heap[count]
            count-=1
            n=1
            while 2*n <= count:
                left,right,smallest=2*n,2*n+1,n
                if heap[left] < heap[smallest]:
                    smallest=left
                if right<=count and heap[right] < heap[smallest]:
                    smallest=right
                if smallest==n:
                    break
                heap[smallest],heap[n]=heap[n],heap[smallest]
                n=smallest

        return curr

        
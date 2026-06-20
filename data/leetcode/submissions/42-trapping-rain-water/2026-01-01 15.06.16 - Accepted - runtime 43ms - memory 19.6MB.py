class Solution:
    def trap(self, height: List[int]) -> int:
        M=len(height)
        if M<=2: return 0
        p=[0]*M
        MAX=-float('inf')
        for m in range(M):
            p[m]=max(0,MAX-height[m])
            MAX=max(MAX,height[m])
        MAX=-float('inf')
        for m in range(M-1,-1,-1):
            p[m]=min(max(0, MAX-height[m]), p[m])
            MAX=max(MAX, height[m])
        return sum(p)
        
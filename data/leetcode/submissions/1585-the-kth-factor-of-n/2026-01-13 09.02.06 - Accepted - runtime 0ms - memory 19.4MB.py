class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        smaller_than_root=[] # including root if int
        larger_than_root=[]
        count=0
        m=1
        while m*m <= n:
            if not n%m:
                smaller_than_root.append(m)
                if m*m<n:
                    larger_than_root.append(n//m)
                count+=1
                if count==k: return m
            m+=1
        count+=len(larger_than_root)
        if count<k: return -1
        return (smaller_than_root+larger_than_root[::-1])[k-1]
class Solution:
    def partitionString(self, s: str) -> int:
        
        count=0
        curr=""
        for c in s:
            if c in curr:
                curr=c
                count+=1
            else:
                curr+=c
        return count+1
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1: return True
        seen_dict={n:True}
        curr=list(map(int, str(n)))
        while True:
            n=sum([m**2 for m in curr])
            if n==1: return True
            if n in seen_dict: return False
            seen_dict[n]=True
            curr=list(map(int, str(n)))
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        r=right
        for i in range(31,-1,-1):
            if (r>>i) & 1 == 0: continue
            if right-left >= (1<<i) or (left>>i & 1 ==0):
                r=r&(~(1<<i))
        return r

class Solution:
    def reverseBits(self, n: int) -> int:
    
        r=0
        for _ in range(32):
            digit=n & 1
            r=(r<<1)|digit
            n=n>>1
        return r
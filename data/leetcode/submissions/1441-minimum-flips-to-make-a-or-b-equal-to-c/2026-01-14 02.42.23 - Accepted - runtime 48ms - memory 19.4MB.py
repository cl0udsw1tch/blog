class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count=0
        while a or b or c:
            c_bit,a_bit,b_bit=c&1,a&1,b&1
            if c_bit:
                if not (a_bit or b_bit): count+=1
            else:
                if a_bit: count+=1
                if b_bit: count+=1

            c,a,b=c>>1,a>>1,b>>1
        return count
            
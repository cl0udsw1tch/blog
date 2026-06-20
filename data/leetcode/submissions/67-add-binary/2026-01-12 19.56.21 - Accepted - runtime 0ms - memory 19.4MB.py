class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        M,N=len(a),len(b)
        
        m,n=M-1,N-1
        r=""
        while m>-1 and n>-1:
            _a, _b=int(a[m]),int(b[n])
            _s=(_a+_b+carry) % 2
            carry=(_a+_b+carry) >> 1
            r=str(_s)+r
            m-=1
            n-=1
        while m>-1:
            _a=int(a[m])
            _s=(_a+carry)%2
            carry=(_a+carry)>>1
            r=str(_s)+r
            m-=1
        while n>-1:
            _b=int(b[n])
            _s=(_b+carry)%2
            carry=(_b+carry)>>1
            r=str(_s)+r
            n-=1

        if carry: r=str(carry)+r
        return r

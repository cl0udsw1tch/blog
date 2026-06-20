class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        if 0<=x<9: return True
        digits=[]
        exp=floor(log10(x))

        while exp>-1:
            digits.append(x//10**exp)
            x=x%10**exp
            exp-=1
        N=len(digits)
        return all([digits[i]==digits[N-i-1] for i in range(N)])
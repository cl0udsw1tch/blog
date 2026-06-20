class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        M=len(digits)
        carry=1
        for m in range(M-1,-1,-1):
            digit=digits[m]
            digits[m]=(digit+carry)%10
            carry=(digit+carry)//10
        if carry:
            digits=[1]+digits
        return digits
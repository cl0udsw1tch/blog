class Solution:
    def intToRoman(self, num: int) -> str:
        conv={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        conv={v: i for i,v in conv.items()}
        arr_num=list(map(int, str(num)))

        M=len(arr_num)

        r=""
        for m in range(M-1,-1,-1):
            digit=arr_num[m]
            POW=M-m-1
            if digit==0:
                continue

            curr=digit*10**POW
            if digit!=4 and digit!=9:
                if curr in conv:
                    r=conv[curr]+r
                elif digit>=5:
                    upper=5*10**POW
                    lower=1*10**POW
                    r=conv[upper]+conv[lower]*(digit-5)+r
                else:
                    lower=1*10**POW
                    r=conv[lower]*digit + r
            else:
                upper=(digit+1)*10**POW
                lower=1*10**POW
                r=conv[lower]+conv[upper]+r
        return r




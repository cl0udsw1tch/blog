class Solution:
    def reverseWords(self, s: str) -> str:
        M=len(s)
        words=[]
        if M==1: return s

        word=""
        m=0
        while m<M:
            if word and s[m]==" ":
                words.append(word)
                word=""
            elif s[m]!=" ":
                word+=s[m]
            m+=1
        if word: words.append(word)
        r=""
        while words:
            r+=words.pop()+" "
        return r[:-1]
            
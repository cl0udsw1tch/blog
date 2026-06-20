class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        M,N=len(word1),len(word2)
        if M==0: return word2
        if N==0: return word1

        r="".join([word1[m]+word2[m] for m in range(min(M,N))])
        r+=word1[min(M,N):] if min(M,N)<M else ""
        r+=word2[min(M,N):] if min(M,N)<N else ""
        return r
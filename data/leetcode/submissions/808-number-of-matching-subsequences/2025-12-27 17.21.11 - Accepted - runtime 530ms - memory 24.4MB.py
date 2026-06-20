class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        M=len(s)
        N=len(words)
     
        dp=[[0] for _ in range(M+1)]
        next=defaultdict(list)
        for word in words:
            next[word[0]].append((word, len(word)))

        total=0
        dp[-1][0]=0
        for m in range(M):
            curr=s[m]
            curr_words=next[curr].copy()
            next[curr]=[]
            for i in range(len(curr_words)):
                word,rem=curr_words[i]
                word,rem=word[1:],rem-1
                if rem==0:total+=1
                else: next[word[0]].append((word,rem))
        return total


        

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        M=len(pattern)
        words=s.split(" ")
        N=len(words)
        if N!=M: return False
        if M==1: return True

        pattern_dict,word_dict={},{}

        for i in range(M):
            c,word=pattern[i],words[i]
            if c in pattern_dict:
                if pattern_dict[c]!=word: return False
            elif word in word_dict:
                return False
            else:
                pattern_dict[c]=word
                word_dict[word]=c
        
        return True


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        M,N,W=len(s),len(words),len(words[0])

        if M==1: return [0] if N==1 and words[0]==s else []

        r=[]
        word_dict=defaultdict(int)
        for word in words:
            word_dict[word]+=1

        for w in range(W):
            ptr1,ptr2=w,w
            seen_dict=defaultdict(int)
            while ptr1<M and ptr2<M:
                curr=s[ptr2:ptr2+W]
                if curr not in word_dict:
                    ptr1=ptr2+W
                    ptr2=ptr1
                    seen_dict=defaultdict(bool)
                else:
                    if seen_dict[curr]<word_dict[curr]:
                        seen_dict[curr]+=1
                        if (ptr2-ptr1)//W +1==N:
                            r.append(ptr1)
                            seen_dict[s[ptr1:ptr1+W]]-=1
                            ptr1+=W
                            ptr2+=W
                        else:
                            ptr2+=W
                    elif seen_dict[curr]==word_dict[curr]:
                        seen_dict[s[ptr1:ptr1+W]]-=1
                        ptr1+=W
        return r

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M,N=len(s),len(t)
        if len(t)>len(s): return ""

        letter_dict=defaultdict(int)
        for c in t:
            letter_dict[c]+=1

        seen_dict=defaultdict(int)
        ptr1,ptr2=0,0
        count, filled=float('inf'), 0
        r=""
        while ptr1<M and ptr2<M+1:
            if s[ptr1] not in letter_dict:
                ptr1+=1
                ptr2=max(ptr2,ptr1)
                
            elif filled==N:
                count=min(count, ptr2-ptr1)
                if count==ptr2-ptr1:
                    r=s[ptr1:ptr2]
                seen_dict[s[ptr1]]-=1
                if seen_dict[s[ptr1]]<letter_dict[s[ptr1]]:
                    filled-=1
                ptr1+=1

            else:
                if ptr2==M: return r

                curr=s[ptr2]
                if curr not in letter_dict:
                    ptr2+=1
                else:
                    if seen_dict[curr]<letter_dict[curr]:
                        filled+=1
                    ptr2+=1
                    seen_dict[curr]+=1
        return r
                

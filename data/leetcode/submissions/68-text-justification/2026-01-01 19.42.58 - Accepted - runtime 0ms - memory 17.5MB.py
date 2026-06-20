class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        M=len(words)
        if M==1: return [words[0]+" "*(maxWidth-len(words[0]))]

        r=[]
        line=[]
        currLen=0
        for m in range(M):
            word=words[m]
            if currLen+len(word)+len(line)>maxWidth:
                extraSpace=maxWidth-currLen
                n_words=len(line)
                n_gaps=n_words-1
                if n_gaps==0:
                    r.append(line[0]+" "*(maxWidth-len(line[0])))
                    line=[word]
                    currLen=len(word)
                    continue

                gapSize=extraSpace//n_gaps
                extra=extraSpace%n_gaps


                for i,seen in enumerate(line[:-1]):
                    line[i]=seen+" "*gapSize
                    if extra:
                        line[i]+=" "
                        extra-=1
                
                r.append("".join(line))
                line=[word]
                currLen=len(word)
            elif currLen+len(line)+len(word)==maxWidth:
                line.append(word)
                r.append(" ".join(line))
                line=[]
                currLen=0
            elif m==M-1:
                line.append(word)
                w=" ".join(line)
                r.append(w+" "*(maxWidth-len(w)))
                line=[]
            else:
                line.append(word)
                currLen+=len(word)
        
        if line:
            r.append(line[0]+ " "*(maxWidth-len(line[0])))

        return r
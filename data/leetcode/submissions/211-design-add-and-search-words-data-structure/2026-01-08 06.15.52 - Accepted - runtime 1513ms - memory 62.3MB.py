class WordDictionary:

    def __init__(self):
        self.edges=[{}]
        self.isword=[False]
        self.count=0

    def addWord(self, word: str) -> None:

        N=len(word)
        n,node=0,0
        while n<N:
            c=word[n]
            if c in self.edges[node]:
                node=self.edges[node][c]
            else:
                self.count+=1
                self.edges.append({})
                self.edges[node][c]=self.count
                self.isword.append(False)
                node=self.count
            n+=1
        self.isword[node]=True
    

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0)

    def search_helper(self, word, node):
        N,n=len(word),0
        while n<N:
            c=word[n]
            if c in self.edges[node]:
                node=self.edges[node][c]
            elif c==".":
                return any([self.search_helper(d+word[n+1:], node) for d in self.edges[node]])
            else:
                return False
            n+=1
        return self.isword[node]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
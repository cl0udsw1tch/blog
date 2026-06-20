class Trie:

    def __init__(self):
        self.edges=[{}]
        self.isword=[False]
        self.count=0

    def insert(self, word: str) -> None:
        N=len(word)
        n=0
        node=0
        while n<N:
            c=word[n]
            if c in self.edges[node]:
                node=self.edges[node][c]
            else:
                self.edges.append({})
                self.count+=1
                self.edges[node][c]=self.count
                self.isword.append(False)
                node=self.count
            n+=1 
        self.isword[node]=True


    def search(self, word: str) -> bool:
        node=0
        N=len(word)
        n=0
        while n<N:
            c=word[n]
            if c not in self.edges[node]: return False
            node=self.edges[node][c]
            n+=1
        return self.isword[node]

    def startsWith(self, prefix: str) -> bool:
        node=0
        N=len(prefix)
        n=0
        while n<N:
            c=prefix[n]
            if c not in self.edges[node]: return False
            node=self.edges[node][c]
            n+=1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
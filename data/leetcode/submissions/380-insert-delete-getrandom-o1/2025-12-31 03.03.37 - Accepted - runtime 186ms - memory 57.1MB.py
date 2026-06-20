class RandomizedSet:
    
    def __init__(self):
        self.MOD=2*10**5
        self.set=[None for _ in range(self.MOD)]
        self.index={}
        self.count=0

    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.set[self.count]=val
            self.index[val]=self.count
            self.count+=1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index:
            idx=self.index[val]
            last_el=self.set[self.count-1]
            self.set[idx] = last_el
            self.index[last_el]= idx
            self.set[self.count-1] = None
            self.count-=1
            del self.index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        i= random.randint(0,self.count-1) if self.count-1>0 else 0
        return self.set[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
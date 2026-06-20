class ProductOfNumbers:

    def __init__(self):
        self.stream=[None for _ in range(4*10**4)] 
        self.zeros_mask=0
        self.n=0
    def add(self, num: int) -> None:
        self.stream[self.n]=(num if num else 1)*(self.stream[self.n-1] if self.n else 1)
        self.zeros_mask=self.zeros_mask<<1
        if num==0:
            self.zeros_mask|=1
        self.n+=1

    def getProduct(self, k: int) -> int:
        if self.zeros_mask&(2**k-1):
            return 0
        if k==self.n:
            return self.stream[self.n-1]
        return self.stream[self.n-1]//self.stream[self.n-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
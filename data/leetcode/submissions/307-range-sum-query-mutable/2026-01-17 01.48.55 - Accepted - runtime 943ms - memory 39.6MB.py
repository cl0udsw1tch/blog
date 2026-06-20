class NumArray:

    def __init__(self, nums: List[int]):
        self.n_leaves=len(nums)
        self.N=4*self.n_leaves
        self.tree=[0]*self.N
        self._build(1, 0,self.n_leaves-1, nums)

    def update(self, index: int, val: int) -> None:
        self._update(1, 0,self.n_leaves-1, index,index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(1, 0,self.n_leaves-1, left,right)

    def _update(self, v:int, vl: int, vr: int, ql: int, qr: int, val: int) -> None: #v=vertex, q=query
        if qr<vl or vr<ql:
            return
        elif vl==vr:
            self.tree[v]=val
        else:
            MID=(vl+vr)//2
            self._update(v*2,vl,MID, ql,qr,val)
            self._update(v*2+1,MID+1,vr,ql,qr,val)
            self.tree[v]=self.tree[v*2]+self.tree[v*2+1]

    def _sumRange(self, v:int, vl: int, vr: int, ql: int, qr: int) -> int:
        if qr<vl or vr<ql: #  handles leaves as well
            return 0
        elif ql<=vl and vr<=qr: #  handles leaves as well
            return self.tree[v]
        else:
            MID=(vl+vr)//2
            return self._sumRange(v*2,vl,MID, ql,qr) + self._sumRange(v*2+1,MID+1,vr,ql,qr)

    def _build(self, v:int, vl: int, vr: int, arr: List[int]) -> None:
        if vl==vr:
            self.tree[v]=arr[vl]
        elif vr<vl:
            return 
        else:
            MID=(vl+vr)//2
            self._build(v*2, vl,MID,arr)
            self._build(v*2+1, MID+1,vr, arr)
            self.tree[v]=self.tree[v*2]+self.tree[v*2+1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
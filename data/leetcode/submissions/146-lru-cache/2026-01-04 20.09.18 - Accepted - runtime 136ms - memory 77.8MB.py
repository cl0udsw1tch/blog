class ListNode:

    def __init__(self,key, val, next=None):
        self.key=key
        self.val=val
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.head=ListNode(key=None, val=None)
        self.tail=self.head
        self.count,self.prev=0,{}
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.prev:
            return -1
        prev=self.prev[key]
        node=prev.next
        next=node.next
        
        if next:
            prev.next=next
            self.prev[next.key]=prev

            self.tail.next=node
            node.next=None
            self.prev[node.key]=self.tail
            self.tail=node
            
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.prev:
            prev=self.prev[key]
            node=prev.next
            node.val=value
            if not node.next:
                return

            node_next=node.next
            prev.next=node_next
            self.prev[node_next.key]=prev

            self.tail.next=node
            self.prev[node.key]=self.tail
            node.next=None
            self.tail=node
            
        else:
            if self.count==self.capacity: 
                LRU=self.head.next
                LRU_key=LRU.key
                del self.prev[LRU_key]
                self.head.next=LRU.next
                if LRU.next:
                    self.prev[LRU.next.key]=self.head
                self.count-=1

                if self.count==0:
                    self.tail=self.head

            node=ListNode(key=key,val=value, next=None)
            self.tail.next=node
            self.prev[key]=self.tail
            self.tail=node
            self.count+=1
  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
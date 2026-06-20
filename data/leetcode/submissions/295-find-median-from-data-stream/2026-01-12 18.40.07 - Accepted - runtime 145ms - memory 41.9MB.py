class MedianFinder:

    def __init__(self):
        self.left_heap=[-float('inf')] # max heap
        self.right_heap=[float('inf')] # min heap
        self.left_count=0
        self.right_count=0

    def addNum(self, num: int) -> None:

        max_left,min_right=self.left_heap[0], self.right_heap[0]
        if self.left_count<self.right_count: #bias to pushing left
            if num<min_right:
                heapq.heappush_max(self.left_heap, num)
                self.left_count+=1
            elif num>=min_right:
                heapq.heappush(self.right_heap,num)
                heapq.heappush_max(self.left_heap, heapq.heappop(self.right_heap))
                self.left_count+=1
        elif self.left_count>=self.right_count: # bias to pushing right
            if num>max_left:
                heapq.heappush(self.right_heap, num)
                self.right_count+=1
            elif num<=max_left:
                heapq.heappush_max(self.left_heap, num)
                heapq.heappush(self.right_heap, heapq.heappop_max(self.left_heap))
                self.right_count+=1


    def findMedian(self) -> float:
        if self.left_count==self.right_count:
            return (1/2)*(self.left_heap[0] + self.right_heap[0])
        elif self.right_count>self.left_count:
            return self.right_heap[0]
        else:
            return self.left_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
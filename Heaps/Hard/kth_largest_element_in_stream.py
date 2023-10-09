import heapq
from typing import List
class KthLargest:
    '''
    in this we only need to ensure that heap contains exactly k elements, so that we can return heap[0]
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        heapq.heapify(self.nums)
        # ensuring that heap contains only k or k-1 elements
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
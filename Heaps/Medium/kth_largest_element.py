from typing import List
import heapq

# # Method - 1
class Solution: # TC -> O(NlogN) and SC -> O(N)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        while k:
            res = heapq.heappop(nums)
            k -= 1
        if res < 0:
            return abs(res)
        return -res
    
# # Method - 2
class Solution: # TC -> O(Nlogk) and SC -> O(k)
    ''' we will maitain an array of length k and it will in decreasing sorted order
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [nums[i] for i in range(k)]
        heapq.heapify(hq)
        for i in range(k,len(nums)):
            if hq[0] < nums[i]:
                heapq.heappop(hq)
                heapq.heappush(hq, nums[i])

        return hq[0]
'''
in min-heap, parent node will always be less than or equal to its children nodes and this is valid to all nodes
nums = [3,2,1,5,6,4]
heapq.heapify(nums)
print(nums) -> [1, 2, 3, 5, 6, 4]
'''

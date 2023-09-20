import heapq
class Solution:
    def kthSmallest(self,nums, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        n = len(nums)
        k = n-k+1
        hq = [nums[i] for i in range(k)]
        heapq.heapify(hq)
        
        for i in range(k,n):
            if hq[0] < nums[i]:
                heapq.heappop(hq)
                heapq.heappush(hq, nums[i])
                
        return hq[0]
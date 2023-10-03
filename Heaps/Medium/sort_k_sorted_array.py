# # https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

import heapq
class Solution:
    '''
    algo: maintain a heap of length of k, once it reaches length k+1, pop from the heap and add it to res
    as every element can be k distance away from its original position, so this will work (in O(NlogK) TC)
    Now once loop is complete, some elements will still be remaining in heap, just pop from it one by one
    and append it to res. 
    '''
    def nearlySorted(self,a,n,k): # TC -> O(Nlogk) and SC -> O(N + k + 1)
        hp = []
        res = []
        hp_len = 0
        for nums in a: # TC -> O(N)
            heapq.heappush(hp, nums) # TC -> O(log(hp_len + 1)) 
            hp_len += 1
            if hp_len > k:
                value = heapq.heappop(hp)
                res.append(value)
                hp_len -= 1
                
        while hp:
            value = heapq.heappop(hp)
            res.append(value)
            
        return res
'''
18. 4Sum

Intuition: The intuition behind this solution is to scale up the Two-Pointer strategy used in 3Sum 
by locking down two stable anchors instead of one, systematically reducing a daunting four-variable 
search into a predictable sorted pair hunt. By sorting the array up front, you gain total control 
over the direction of your sums and can easily isolate unique combinations. The algorithm uses two 
nested loops to establish a rock-solid foundation: the outer loop fixes the first element (nums[ind]), 
and the inner loop fixes a second element (nums[next_ind]) right ahead of it. With these two values 
safely anchored as a constant baseline, the remaining sub-problem collapses into a classic Two-Sum 
target hunt, where a start pointer at the left boundary and an end pointer at the right boundary 
gracefully close in on each other. Because the numbers are sorted, you simply slide start forward 
to boost a sum that is too low (total < target) or shrink end inward to suppress a sum that is too 
high (total > target). To guarantee that the final list contains zero duplicate quadruplets, the 
algorithm aggressively skips over identical values at every single layer—when moving the first anchor, 
when moving the second anchor, and right after discovering a valid target match—ensuring complete 
structural uniqueness without relying on an expensive post-processing set.
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for ind in range(n-3):
            if ind>0 and nums[ind] == nums[ind-1]:
                continue
            for next_ind in range(ind+1, n-2):
                if next_ind>ind+1 and nums[next_ind] == nums[next_ind-1]:
                    continue
                start = next_ind+1
                end = n - 1

                while end>start:
                    total = nums[ind] + nums[next_ind] + nums[start] + nums[end]
                    if total > target:
                        end-=1
                    elif total < target:
                        start+=1
                    else:
                        res.append([nums[ind], nums[next_ind], nums[start], nums[end]])
                        start+=1
                        while end>start and nums[start]==nums[start-1]:
                            start+=1
        
        return res

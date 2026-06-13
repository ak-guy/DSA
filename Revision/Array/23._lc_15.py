'''
15. 3Sum

Intuition: The intuition behind this solution is to reduce a complex three-number search into a 
manageable series of Two-Pointer lookups by first stabilizing the array through sorting. Sorting 
the numbers allows you to systematically fix one element (nums[ind]) as a permanent baseline 
anchor during each iteration of a loop and then treat the remaining problem as a classic, sorted 
Two-Sum hunt. With the anchor fixed, you place a start pointer right next to it and an end pointer 
at the absolute back of the array; because the values are sorted, a combined sum that is too low 
(total < 0) tells you to greedily step your start pointer forward to find larger numbers, while a 
sum that is too high (total > 0) tells you to shrink your end pointer inward to find smaller numbers. 
To meet the strict requirement of returning only unique triplets, the algorithm cleverly bypasses 
duplicates by skipping over identical values whenever the anchor moves forward (nums[ind-1] == nums[ind]) 
or whenever a successful zero-sum match is found and the start pointer shifts, perfectly filtering out 
repetitive combinations in linear time per anchor.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for ind in range(n-2):
            if ind > 0 and nums[ind-1] == nums[ind]:
                continue

            start, end = ind+1, n-1
            while start < end:
                total = nums[ind] + nums[start] + nums[end]
                if total == 0:
                    result.append([nums[ind], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif total < 0:
                    start += 1
                else:
                    end -= 1
        
        return result

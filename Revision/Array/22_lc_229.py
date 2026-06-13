'''
229. Majority Element II

Intuition: The intuition behind this solution—an extension of the Boyer-Moore Majority Vote Algorithm—is 
based on a political battleground theory where opposing factions cancel each other out, leveraging the 
mathematical certainty that an array can contain at most two distinct elements that appear strictly more 
than one-third of the time (>⌊n/3⌋). You maintain up to two leading candidates and their voting strengths 
(count1, count2), treating the array as a sequence of votes: if a number matches an active candidate, 
their strength grows; if a candidacy slot sits empty, the new number immediately claims it; and if a number 
matches neither candidate while both slots are occupied, it triggers a mutual three-way standoff where 
both candidates lose one point of strength. Because the true majority elements each occupy more than 33.3% 
of the total real estate, they possess enough raw volume to survive these collective eliminations and remain 
standing at the end. Since this survival process only identifies the top two potential contenders, a quick 
verification pass using .count() is required at the end to confirm they actually crossed the strict ⌊n/3⌋ 
threshold.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result
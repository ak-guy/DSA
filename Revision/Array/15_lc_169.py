'''
169. Majority Element

Intuition: The intuition behind this solution—known as Boyer-Moore Voting Algorithm—is to view the 
array as a political battleground where different numbers vote for themselves, and because the 
majority element appears more than half the time, it can successfully out-vote and survive all 
other numbers combined. You establish a running majority candidate and a count representing their 
current political strength or lead. As you iterate through the list, every time you see a number 
hat matches the candidate, their strength increases (count += 1), and every time you see an opposing 
number, they cancel each other out by sacrificing one point of strength (count -= 1). If the current 
candidate's strength drops entirely to zero, it means they have been completely neutralized by the 
opposition, prompting the very next number to step up and claim the throne as the new candidate. 
Because the true majority element occupies more than 50% of the total real estate, it possesses 
enough raw volume to survive all these mutual eliminations and will inevitably be the last candidate 
standing when the loop finishes.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = nums[0]
        count = 0
        for i in nums:
            if majority == i:
                count += 1
            elif count == 0:
                majority = i
            else:
                count -= 1
        return majority

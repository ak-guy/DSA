'''
2100. Find Good Days to Rob the Bank
'''

'''
This solution identifies "good days" to rob the bank by precomputing two arrays 
that track non-increasing sequences before each day and non-decreasing sequences 
after each day in the security array. The pre array counts how many consecutive 
days up to the current day have non-increasing security values, while the post 
array counts how many consecutive days from the current day onward have 
non-decreasing security values. A day is considered good if both counts exceed 
the given time, ensuring the security levels meet the required conditions for 
time days before and after that day. The indices of all such good days are 
collected and returned.
'''

class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        pre = [1 for _ in range(n)]
        for i in range(1, n):
            if security[i-1] >= security[i]:
                pre[i] = pre[i-1]+1
        
        post = [1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if security[i+1] >= security[i]:
                post[i] = post[i+1]+1
        
        result = []
        for i in range(n):
            if pre[i] > time and post[i] > time:
                result.append(i)
        
        return result
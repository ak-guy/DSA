'''
1947. Maximum Compatibility Score Sum
'''

from typing import List

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        perms = []

        def getPermutations(i, arr):
            if i == n:
                perms.append(arr[::])
                return
            
            for ind in range(i,n):
                arr[ind], arr[i] = arr[i], arr[ind]
                getPermutations(i+1, arr)
                # backtrack
                arr[ind], arr[i] = arr[i], arr[ind]

        getPermutations(0, [i for i in range(n)])

        res = 0
        for perm in perms: # 8!
            total = 0
            for i in range(n): # 8
                currMentor = mentors[perm[i]]
                currStudent = students[i]
                start = 0
                count = 0
                while start < m: # 8
                    if currMentor[start] == currStudent[start]:
                        count +=1
                    start += 1
                total += count
            res = max(res, total)
            
        return res

'''
2326. Spiral Matrix IV
'''
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        start_row, start_col = 0, 0
        end_row, end_col = m-1, n-1

        res = [[-1 for c in range(n)] for r in range(m)]

        while head:
            for col in range(start_col, end_col+1):
                if not head: break
                res[start_row][col] = head.val
                head = head.next
            # print(f'l -> r = {res}')
            for row in range(start_row+1, end_row+1):
                if not head: break
                res[row][end_col] = head.val
                head = head.next
            # print(f't -> b = {res}')
            for col in range(end_col-1, start_col-1, -1):
                if not head: break
                res[end_row][col] = head.val
                head = head.next
            # print(f'r -> l = {res}')
            for row in range(end_row-1, start_row, -1):
                if not head: break
                res[row][start_col] = head.val
                head = head.next
            # print(f'b -> t = {res}')
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
            # print(res)
        
        return res
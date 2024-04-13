'''
ll = [0] + [5,2,6,3,9,1,7,3,8,4]

curr2_val = 0, temp_nodes_to_traverse = 1
number_of_nodes_to_traverse = 1, curr1_val = 0, curr2_val == 5, number_of_nodes_we_were_able_to_traverse = 1

curr2_val = 5, temp_nodes_to_traverse = 2
number_of_nodes_to_traverse = 2, curr1_val = 5, curr2_val == 6, number_of_nodes_we_were_able_to_traverse = 2

curr2_val = 6, temp_nodes_to_traverse = 3
number_of_nodes_to_traverse = 3, curr1_val = 6, curr2_val == 9, number_of_nodes_we_were_able_to_traverse = 3

curr2_val = 9, temp_nodes_to_traverse = 4
number_of_nodes_to_traverse = 4, curr1_val = 9, curr2_val == 8, number_of_nodes_we_were_able_to_traverse = 4

curr2_val = 8, temp_nodes_to_traverse = 5
number_of_nodes_to_traverse = 5, curr1_val = 8, curr2_val == 4, number_of_nodes_we_were_able_to_traverse = 4

curr2_val = 4, temp_nodes_to_traverse = 6
number_of_nodes_to_traverse = 6, curr1_val = 4, curr2_val == 3, number_of_nodes_we_were_able_to_traverse = 3
'''
from __future__ import annotations

from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)

        number_of_nodes_to_traverse = 1
        curr1 = dummy
        curr2 = dummy

        while curr1 and curr1.next:
            number_of_nodes_we_were_able_to_traverse = 0
            temp_nodes_to_traverse = number_of_nodes_to_traverse
            # print(f'curr2_val = {curr2.val}, temp_nodes_to_traverse = {temp_nodes_to_traverse}')
            while curr2 and curr2.next and temp_nodes_to_traverse:
                curr2 = curr2.next
                number_of_nodes_we_were_able_to_traverse += 1
                temp_nodes_to_traverse -= 1

            is_even_length = not number_of_nodes_we_were_able_to_traverse % 2
            # print(f'number_of_nodes_to_traverse = {number_of_nodes_to_traverse}, curr1_val = {curr1.val}, curr2_val == {curr2.val}, number_of_nodes_we_were_able_to_traverse = {number_of_nodes_we_were_able_to_traverse}')
            if is_even_length:

                '''
                1. curr1 points to the node just before left of what starting point of nodes which we have to reverse
                2. curr2 points to the node till which we have to reverse

                reverse -> [curr1.next, curr2]
                '''
                prev = None
                node_to_left = curr1
                store_next_pointer = node_to_left.next
                temp_curr = curr1
                temp_curr = temp_curr.next
                for i in range(number_of_nodes_we_were_able_to_traverse):
                    temp_next_ptr = temp_curr.next
                    temp_curr.next = prev
                    prev = temp_curr
                    temp_curr = temp_next_ptr

                curr1 = store_next_pointer
                node_to_left.next = prev
                store_next_pointer.next = temp_next_ptr
                curr2 = store_next_pointer
            else:
                while number_of_nodes_we_were_able_to_traverse:
                    curr1 = curr1.next
                    number_of_nodes_we_were_able_to_traverse -= 1

            number_of_nodes_to_traverse += 1
        return dummy.next

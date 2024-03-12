# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convert_ll_to_array(self, node):
        resultant_array = []
        modified_val = 0
        while node:
            modified_val += node.val
            resultant_array.append(modified_val)
            node = node.next
        return resultant_array

    def convert_array_to_ll(self, arr):
        head = ListNode(arr[0])
        dummy_head = head
        for ind in range(1, len(arr)):
            new_node = ListNode(arr[ind])
            dummy_head.next = new_node
            dummy_head = new_node
        
        return head

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr_repr = self.convert_ll_to_array(head)
        if len(arr_repr) == 1 and arr_repr[0] == 0:
            return None
        print(arr_repr)
        start_ind = 0
        test_set = set()
        test_set.add(arr_repr[0])
        res = [arr_repr[0]] if arr_repr[0] != 0 else []
        for ind in range(1,len(arr_repr)):
            if arr_repr[ind] == 0:
                res = []
                test_set = set()
                continue
            if arr_repr[ind] in test_set:
                poping_ind = len(res)-1
                while poping_ind >=0 and arr_repr[ind] != res[poping_ind]:
                    res.pop()
                    test_set.remove(arr_repr[poping_ind])
                    poping_ind -= 1
                continue
            res.append(arr_repr[ind])
            test_set.add(arr_repr[ind])

        if len(res) == 0:
            return None
        print(res)
        temp = res[0]
        for ind in range(1, len(res)):
            new_temp = res[ind]
            res[ind] -= temp
            temp = new_temp
        print(res)
        new_head = self.convert_array_to_ll(res)
        return new_head
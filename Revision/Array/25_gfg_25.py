"""
GFG: Count Subarrays with given XOR

Intuition: The intuition behind this solution relies on a brilliant algebraic property of the 
XOR operation: if you know the total XOR of a prefix, you can instantly deduce the exact missing 
piece needed to form your target subarray. Any contiguous subarray's XOR sum can be isolated by 
stripping away an earlier prefix from the current cumulative running_xor. Mathematically, if a 
target middle subarray has a value of k, then the relationship can be written as Prefix 
XOR⊕k=Running XOR, which rearranges beautifully via XOR logic into Prefix XOR=Running XOR⊕k. 
By maintaining a fast-lookup hash map (occurence_map) that logs the frequencies of every prefix 
XOR encountered so far, the algorithm doesn't need to manually scan backward; at each step, it 
calculates the exact required prefix (lookup) and instantly adds its historical frequency to the 
total count (res). This completely eliminates the need for nested loops, turning a complex 
structural search into a single, efficient linear pass that catches every valid subarray combination 
effortlessly.
"""

class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        running_xor = 0
        res = 0
        occurence_map = {0:1}

        for val in arr:
            running_xor ^= val
            lookup = running_xor ^ k
            res += occurence_map.get(lookup, 0)
            occurence_map[running_xor] = occurence_map.get(running_xor,0) + 1

        return res

if __name__ == '__main__':
    obj = Solution()

    res = obj.subarrayXor([4, 2, 2, 6, 4], 6)
    assert res == 4

    res = obj.subarrayXor([5, 6, 7, 8, 9], 5)
    assert res == 2

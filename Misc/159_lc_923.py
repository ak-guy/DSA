from collections import defaultdict

"""
923. 3Sum With Multiplicity

This solution solves the 3Sum Multi problem by combining an iterative search with combinatorial counting to efficiently handle duplicate values.
After sorting the array and building a frequency map, the algorithm iterates through each element to treat it as the first member of a potential 
triplet, temporarily removing it from the map to maintain the i<j<k index constraint. For the remaining two elements, it iterates through the 
unique keys in the map and calculates the necessary third value (target-first-second); if that value exists, it calculates the number of possible 
combinations—using count1 * count2 for distinct values or n(n-1) for identical ones—and adds them to a running total. By operating on unique keys 
for the second and third elements rather than raw indices, the approach significantly reduces redundant calculations, finally returning the 
total count modulo 109+7 after adjusting for double-counting.

The reason the final result is divided by 2 is that the nested loops treat the second and third elements as an ordered pair rather than an 
unordered set. While the first element is fixed by the outer loop, the inner loops iterate through the count_map and check for key and 
required_key. If these two numbers are different, the code will eventually encounter them twice: once when the inner loop hits the first 
number (treating it as key) and once when it hits the second number (treating it as key). By calculating the product of their frequencies 
both times and summing them, the algorithm double-counts every valid (j,k) pair, necessitating the floor division by 2 at the end to arrive 
at the correct number of unique triplets.
"""


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        result = 0
        count_map = defaultdict(int)
        mod = 1_000_000_007
        for val in arr:
            count_map[val] += 1

        for first in range(n - 2):
            curr = arr[first]
            count_map[curr] -= 1
            if count_map[curr] == 0:
                count_map.pop(curr)

            for key, val in count_map.items():
                required_key = target - curr - key
                if required_key not in count_map:
                    continue
                if required_key != key:
                    result += (count_map[required_key] * count_map[key]) % mod
                else:
                    result += (
                        count_map[required_key] * (count_map[required_key] - 1)
                    ) % mod

        return (result % mod) // 2
